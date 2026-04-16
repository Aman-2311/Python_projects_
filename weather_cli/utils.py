import requests

from config import API_KEY, BASE_URL

def get_weather(city):
    if not API_KEY:
        return {"error": "API key missing. Add API_KEY in weather_cli/.env"}

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        result = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"],
        }
        return result

    except requests.exceptions.HTTPError:
        return {"error": "City not found or API error"}

    except requests.exceptions.RequestException:
        return {"error": "Network error"}

