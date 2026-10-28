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
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("Не задан ключ OPENWEATHER_API_KEY")

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
            logging.info("Погода для города %s успешно получена", city)
            return {
                "city": data["name"],
                "temp": round(data["main"]["temp"]),
                "desc": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"]
            }
        logging.warning(
            "OpenWeatherMap вернул статус %s для города %s",
            response.status_code,
            city,
        )
        return None
    except requests.exceptions.RequestException:
        logging.exception("Ошибка запроса погоды для города %s", city)
        return None
