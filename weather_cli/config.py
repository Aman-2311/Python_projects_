#read .env variable
from dotenv import load_dotenv
load_dotenv()
#acess env variable
import os
API_KEY = os.get("API_KEY")
#path-endpoint to follow
BASE_URl = "http://api.openweathermap.org/data/2.5/weather?"
