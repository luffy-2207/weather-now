from weather_api import get_weather

def display_weather(weather):
    if "error" in weather:
        print(f"\nError: {weather['error']}")
    else:
        print("\n--- Weather Details ---")
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Weather: {weather['weather']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
        print("-----------------------\n")

def main():
    print("Welcome to Weather-Now!")
    API_KEY = "98c1c1bfd020ff1a880bd59d9eae7c0b"  # Replace with your API key
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye! Stay safe!")
            break
        weather = get_weather(city, API_KEY)
        display_weather(weather)

if __name__ == "__main__":
    main()