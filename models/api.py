import requests

API_KEY = "ВАШ_API_КЛЮЧ"

def fetch_weather(city: str) -> dict | None:
    """Делает запрос к API и возвращает только нужные данные или None."""
    url = f"https://openweathermap.org{city}&appid={API_KEY}&units=metric&lang=ru"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temp": round(data["main"]["temp"]),
                "desc": data["weather"]["description"].capitalize(),
                "humidity": data["main"]["humidity"]
            }
        return None
    except requests.exceptions.RequestException:
        return None
