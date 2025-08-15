from twilio.rest import Client
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
import time

# --- Twilio Setup ---
TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH = "YOUR_TWILIO_AUTH"
TWILIO_NUMBER = "+1234567890"
MY_NUMBER = "+2348012345678"
twilio_client = Client(TWILIO_SID, TWILIO_AUTH)

# --- Google Calendar Setup ---
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
SERVICE_ACCOUNT_FILE = "service_account.json"
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
calendar_service = build("calendar", "v3", credentials=creds)

def get_upcoming_events(minutes_ahead=15):
    now = datetime.datetime.utcnow().isoformat() + "Z"
    future = (datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes_ahead)).isoformat() + "Z"
    events_result = calendar_service.events().list(
        calendarId="primary", timeMin=now, timeMax=future,
        singleEvents=True, orderBy="startTime"
    ).execute()
    return events_result.get("items", [])

def call_reminder(event):
    twilio_client.calls.create(
        to=MY_NUMBER,
        from_=TWILIO_NUMBER,
        twiml=f'<Response><Say voice="alice">Reminder: {event["summary"]} is starting soon.</Say></Response>'
    )

while True:
    events = get_upcoming_events()
    for event in events:
        start_time = event["start"]["dateTime"]
        print(f"Calling reminder for: {event['summary']} at {start_time}")
        call_reminder(event)
    time.sleep(60)  # check every minute
