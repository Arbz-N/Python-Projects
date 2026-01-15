Weather App using Python & OpenWeather API

    This project is a simple Python-based weather application that fetches real-time weather information for any city using the OpenWeather API.

It demonstrates how to::

    Use environment variables securely with a .env file
    Call a public REST API using requests
    Parse JSON responses in Python
    Follow best practices by keeping API keys out of source code

Features

    Get current weather condition of any city
    Displays temperature in Celsius
    Uses .env file to protect API keys
    Beginner-friendly and easy to extend

Project Structure
    weather-app/
    
     -.env              # Stores API key 
     -weather.py        # Main Python script
     -README.md         #to overview

Environment Variables

    Create a .env file in the project root:
    OPENWEATHER_API_KEY=your_real_api_key_here

How to Generate OpenWeather API Key

    Go to OpenWeather
    and sign up for a free account.
    After logging in, go to API Keys tab.
    Click Generate Key or copy the default key.
    Paste this key into your .env file as OPENWEATHER_API_KEY.
    Now your Python app can securely access the API without exposing the key.

Important:

    Never upload .env to GitHub.
    Your .gitignore file should contain:
    .env

Prerequisites

    Make sure you have:
    Python 3 installed
    An OpenWeather account
    Required Python packages
    Install dependencies:
    pip install requests python-dotenv

How to Run the Project

    Clone the repository
    Add your API key in .env
    Run the script:
    python script.py


    Enter a city name when prompted:
    Enter the name of City - London

Sample Output

    Weather in London: 18.45°C with clear sky
    If city name is incorrect:
    City name 'abcxyz' is not found or incorrect

📝 Notes

    Read the code carefully before running it
    This project is for learning & practice
    API responses are in Kelvin, converted to Celsius manually
    You can extend this app to show humidity, wind speed, or forecasts

