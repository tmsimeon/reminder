# 📞 Persistent Voice Reminder App

A Python-based **voice reminder system** that connects to your **Google Calendar**, checks upcoming events, and **calls your phone** to remind you.  
If you don’t pick up or acknowledge the call, it **keeps calling** until the event is over.

---

## 🚀 Features
- **Google Calendar Integration** – Reads events and their start/end times.
- **Automated Calls** – Uses Twilio Voice API (or Plivo/Vonage) to place reminder calls.
- **Text-to-Speech** – Speaks event details to you over the phone.
- **Retry Until Answered** – Keeps calling if you don’t answer.
- **Voice Command Acknowledgment** – Stops calling when you say a keyword (e.g., “Got it”).
- **Configurable Reminder Time** – Set how many minutes before an event you get a call.
- **Runs 24/7** – Works continuously when deployed on a server.

---

## 🛠 Tech Stack
- **Python 3.9+**
- **Google Calendar API** (event fetching)
- **Twilio Voice API** (phone calls & TTS)
- **SQLite / PostgreSQL** (track calls and statuses)
- **APScheduler** (scheduling checks)

---

## 📋 Prerequisites

1. **Python 3.9+**
2. **Google Cloud Project** with Calendar API enabled
3. **Twilio Account** (or alternative telephony API)
4. A **Twilio phone number** capable of making outbound calls
5. Basic understanding of Python virtual environments

---

## ⚙️ Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/tmsimeon/reminder.git
cd reminder
