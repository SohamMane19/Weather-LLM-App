import requests
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str) -> str:
    """
    Fetches current weather for a given city using OpenWeatherMap API.
    Always returns a clean string (never raises).
    """
    if not OPENWEATHER_API_KEY:
        return "Weather service is not configured properly."

    
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return f"Unable to fetch weather data for {city}."

    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"It’s {temp}°C with {desc} in {city.capitalize()}."
