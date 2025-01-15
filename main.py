import sys
from weather_app import load_api_key, get_weather

def display_weather(weather):
    if "error" in weather:
        print(f"\nError: {weather['error']}")
    else:
        print("\n--- Weather Details ---")
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}\u00b0C")
        print(f"Weather: {weather['weather']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
        print("-----------------------\n")

def main():
    print("Welcome to Weather-Now!")

    API_KEY = load_api_key()
    if not API_KEY:
        print("Error: API key not found...")
        sys.exit(1)


    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye! Stay safe!")
            break
        if not city:
            print("City name cannot be empty. Please try again.")
            continue
        weather = get_weather(city, API_KEY)
        display_weather(weather)

if __name__ == "__main__":
    main()
