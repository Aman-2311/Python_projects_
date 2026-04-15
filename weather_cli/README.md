# Weather CLI App

## 📌 Description
A Python command-line application that fetches real-time weather data using OpenWeather API.

---

## 🚀 Features
- Get weather by city name
- Shows temperature, humidity, and condition
- Handles errors (invalid city, network issues)

---

## 🛠 Tech Stack
- Python
- Requests
- Python-dotenv

---

## 📁 Project Structure
weather_cli/
│
├── main.py
├── utils.py
├── config.py
├── .env
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

1. Clone repo:
   git clone <your-repo-link>

2. Install dependencies:
   pip install -r requirements.txt

3. Add API key in `.env`:
   API_KEY=your_api_key

4. Run:
   python main.py Pune

---

## 📌 Example Output
City: Pune  
Temperature: 28°C  
Humidity: 60%  
Condition: Cloudy