import os
from pathlib import Path

from dotenv import load_dotenv

# Always load .env from this file's directory so running from project root works.
ENV_PATH = Path(__file__).resolve().with_name(".env")
load_dotenv(dotenv_path=ENV_PATH)

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
