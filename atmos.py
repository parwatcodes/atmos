#!/usr/bin/env python3

import requests
import argparse
import os
from datetime import datetime
from colorama import Fore, Style
from dotenv import load_dotenv

# Load env variables from .env file
load_dotenv()

api_key = os.getenv('API_KEY')
base_url = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
  url = f"{base_url}?q={city}&appid={api_key}&units=metric"

  try:
      response = requests.get(url)
      response.raise_for_status()

      return response.json()
  except requests.exceptions.HTTPError as http_err:
    print(Fore.RED + f"HTTP error occurred: {http_err}" + Style.RESET_ALL)
  except Exception as err:
    print(Fore.RED + f"Other error occurred: {err}" + Style.RESET_ALL)

def display_weather(data, city):
    """Format and print the weather information."""
    print(Fore.CYAN + f"\nWeather Report for {city.capitalize()}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Temperature: {data['main']['temp']}°C" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Humidity: {data['main']['humidity']}%" + Style.RESET_ALL)
    print(Fore.BLUE + f"Pressure: {data['main']['pressure']} hPa" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"Wind Speed: {data['wind']['speed']} m/s" + Style.RESET_ALL)
    print(Fore.CYAN + f"Description: {data['weather'][0]['description']}" + Style.RESET_ALL)
    sunrise_time = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
    sunset_time = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
    print(Fore.RED + f"Sunrise: {sunrise_time}" + Style.RESET_ALL)
    print(Fore.RED + f"Sunset: {sunset_time}" + Style.RESET_ALL)


def main():
    # Setup command-line arguments
    parser = argparse.ArgumentParser(description="CLI Weather App")
    parser.add_argument("-c", "--city", type=str, required=True, help="City name to get the weather for")
    args = parser.parse_args()

    # Fetch and display weather
    weather_data = get_weather(args.city)
    if weather_data and weather_data.get('main'):
        display_weather(weather_data, args.city)
    else:
        print(Fore.RED + "Could not retrieve weather data. Please check the city name and try again." + Style.RESET_ALL)

# This block ensures that the main() function is only called when the script is run directly,
# and not when it is imported as a module in another script.
if __name__ == "__main__":
    main()
