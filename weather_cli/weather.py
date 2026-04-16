import sys

from utils import get_weather

def main():
    if len(sys.argv) < 2:
        print("usage: python weather.py <city>")
        return

    city = sys.argv[1]
    result = get_weather(city)

    if "error" in result:
        print(result["error"])
    else:
        print(f"city: {result['city']}")
        print(f"temp: {result['temp']} C")
        print(f"humidity: {result['humidity']}%")
        print(f"condition: {result['condition']}")

if __name__ == "__main__":
    main()
