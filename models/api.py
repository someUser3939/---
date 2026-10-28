import os
import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def fetch_weather(city: str) -> dict | None:
    """Делает запрос к API и возвращает только нужные данные или None."""
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = os.getenv("b3433d45eb2e920808467ffe4af32cc8")
    if not api_key:
        raise RuntimeError("Не задан ключ OPENWEATHER_API_KEY")
        logging.info('api не задан')

    
    try:
        response = requests.get(
            url,
            params={
                "q": city,
                "appid": api_key,
                "units": "metric",
                "lang": "ru",
            },
            timeout=10,
        )
        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temp": round(data["main"]["temp"]),
                "desc": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"]
            }
        return None
        logging.info('requests complete')
    except requests.exceptions.RequestException:
        return None
        logging.info('erro requests')
