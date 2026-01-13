# WeatherPulse CLI  
*A Professional Command-Line Weather Data Collector*

---

## Overview
WeatherPulse CLI is a production-ready Python command-line application that retrieves real-time weather data from the OpenWeatherMap API and stores it in structured JSON format. The tool is designed for developers, system engineers, and learners who want a clean example of API integration, secure configuration handling, and professional-grade logging in a CLI environment.

---

## Key Features
- Secure API key management using environment variables  
- Command-line interface with argument validation  
- Real-time weather data retrieval  
- Structured JSON output  
- Centralized logging for debugging and monitoring  
- Clean, modular, and production-style codebase  

---

## Prerequisites

Ensure you have:

- Python **3.8+**
- An API key from **OpenWeatherMap**
- Installed dependencies:
  - `requests`
  - `python-dotenv`

Install dependencies:

```bash
pip install requests python-dotenv
Project Structure
bash
Copy code
.
├── weatherpulse_cli.py
├── weatherpulse.log
├── .env
└── README.md
Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/weatherpulse-cli.git
cd weatherpulse-cli
2. Create .env file
env
Copy code
WEATHER_API_KEY=your_api_key_here
3. Secure sensitive files
Add this to .gitignore:

bash
Copy code
.env
*.log
Usage
Run from terminal:

bash
Copy code
python weatherpulse_cli.py --city London --file_path london_weather.json