import requests
import json
import argparse
import logging
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")   # Your API key goes in .env file
# ===========================================


def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")

    except Exception as err:
        logging.error(f"Unexpected error occurred: {err}")


def save_data_to_file(data, file_path):
    try:
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        logging.info(f"Data successfully saved to {file_path}")

    except Exception as e:
        logging.error(f"Error saving data: {e}")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="WeatherPulse CLI - Professional Weather Data Fetcher"
    )
    parser.add_argument(
        "--file_path",
        type=str,
        required=True,
        help="Destination path for saving JSON output",
    )
    parser.add_argument(
        "--city",
        type=str,
        required=True,
        help="City name to fetch weather data for",
    )
    return parser.parse_args()


def build_weather_url(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    return f"{BASE_URL}?q={city}&appid={API_KEY}"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="weatherpulse.log",
)


if __name__ == "__main__":
    args = parse_arguments()

    logging.info("WeatherPulse CLI started...")

    url = build_weather_url(args.city)
    data = fetch_data(url)

    if data:
        save_data_to_file(data, args.file_path)
