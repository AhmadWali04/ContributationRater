import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Discord Bot Environment Variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
DISCORD_GUILD_ID = os.getenv("DISCORD_GUILD_ID", "")
DISCORD_BOT_ID = os.getenv("DISCORD_BOT_ID", "")

# Database Environment Variables
DATABASE_URL = os.getenv("DATABASE_URL", "")
DATABASE_AUTH_TOKEN = os.getenv("DATABASE_AUTH_TOKEN", "")
SQL_ECHO = os.getenv("SQL_ECHO", "false").lower() == "true"

# API Environment Variables
API_ENABLED = os.getenv("API_ENABLED", "true").lower() == "true"
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
API_BASE_URL = os.getenv("API_BASE_URL", "/api")

# Frontend | Backend Environment Variables
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:3000")

# Logging Environment Variables
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Google Sheets API Environment Variables
GOOGLE_SHEETS_ENABLED = os.getenv("GOOGLE_SHEETS_ENABLED", "false").lower() == "true"
GOOGLE_SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_CREDENTIALS", "")
GOOGLE_SHEETS_SPREADSHEET_ID = os.getenv("GOOGLE_SHEETS_SPREADSHEET_ID", "")

# Activity Tracking Environment Variables
ACTIVITY_TRACKING_ENABLED = os.getenv("ACTIVITY_TRACKING_ENABLED", "true").lower() == "true"
ACTIVITY_TRACKING_INTERVAL = int(os.getenv("ACTIVITY_TRACKING_INTERVAL", "60")) # sec/min
ACTIVITY_TRACKING_CHANNELS = os.getenv("ACTIVITY_TRACKING_CHANNELS", "").split(",")

# ML/AI Environment Variables
AI_REPORTS_ENABLED = os.getenv("AI_REPORTS_ENABLED", "true").lower() == "true"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

ML_ENABLED = os.getenv("ML_ENABLED", "false").lower() == "true"
ML_MODEL_PATH = os.getenv("ML_MODEL_PATH", str(BASE_DIR / "models"))
ML_PREDICTION_INTERVAL = int(os.getenv("ML_PREDICTION_INTERVAL", "86400")) # sec/day

# Command Cooldown Environment Variables
COOLDOWN_ACTIVITY = int(os.getenv("COOLDOWN_ACTIVITY", "5"))
COOLDOWN_REPORT = int(os.getenv("COOLDOWN_REPORT", "30"))
COOLDOWN_ADMIN = int(os.getenv("COOLDOWN_ADMIN", "3"))

# Feature Flags Environment Variables
FEATURE_VOICE_TRACKING = os.getenv("FEATURE_VOICE_TRACKING", "true").lower() == "true"
FEATURE_REACTION_TRACKING = os.getenv("FEATURE_REACTION_TRACKING", "true").lower() == "true"
FEATURE_PRESENCE_TRACKING = os.getenv("FEATURE_PRESENCE_TRACKING", "true").lower() == "true"
FEATURE_DASHBOARD_INTEGRATION = os.getenv("FEATURE_DASHBOARD_INTEGRATION", "true").lower() == "true"
