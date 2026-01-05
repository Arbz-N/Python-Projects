import requests
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

#
api_key = os.getenv("OPENWEATHER_API_KEY") #fetch from .env file
city_name = input("Enter the name of City - ")


url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

response = requests.get(url)
if response.status_code == 200: #check the condition
    weather_data = response.json()
    weather_disc = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp'] - 273.15 #converted to Celsius manually

    #display weather info
    print(f"Weather in {city_name}: {round(temp,2)}°C with {weather_disc}")
else:
    print(f"City name: {city_name} is not found or incorrect")
