# Make sure you have the requests library installed: pip install requests

import requests

def get_weather(latitude, longitude, api_key):
  url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error getting weather data: {response.status_code}")
    return None

# Replace with your actual location retrieval logic (e.g., from user input)
latitude = 40.7128  # Example latitude (New York City)
longitude = -74.0059  # Example longitude (New York City)
api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

weather_data = get_weather(latitude, longitude, api_key)

if weather_data:
  city = weather_data["name"]
  temp = round(weather_data["main"]["temp"] - 273.15, 2)  # Convert Kelvin to Celsius with 2 decimals
  weather = weather_data["weather"][0]["main"]
  print(f"Weather in {city}: Temperature - {temp}°C, Weather - {weather}")
else:
  print("Failed to retrieve weather data.")
