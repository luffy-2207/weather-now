import requests
import configparser

def load_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get('DEFAULT', 'API_KEY', fallback=None)


def get_weather(city, api_key):
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Metric units for temperature (Celsius)
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        
        # Extract relevant weather details
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return weather

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}
    except KeyError as e:
        return {"error": f"Missing expected data in response: {e}"}


