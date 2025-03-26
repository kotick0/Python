import requests as req
from tabulate import tabulate
import time
import os

# OpenWeather variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = str(input("Please input your city: ").title())
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Function: validate city input
def validate_city_input():
    url = f"{BASE_URL}?q={CITY}&appid={API_KEY}&units=metric"
    response = req.get(url)
    data = response.json()

    if response.status_code == 404:
        return False
    else:
        return True


# Function: validate API functtion
def validate_api(api_key):
    url = f"{BASE_URL}?q=Warsaw&appid={api_key}&units=metric"
    response = req.get(url)
    data = response.json()

    if response.status_code == 401:
        return False, data.get("message", "Invalid API Key.")
    return True, None


# Check whether API_KEY is present and is correct
if not API_KEY:
    print("Error: API key is missing, set OPENWEATHER_API_KEY environment variable.")
    exit()
else:
    is_valid, error_message = validate_api(API_KEY)
    if not is_valid:
        print(f"Error: {error_message}")
        exit()
# Validate city name
if not validate_city_input():
    print("Provided city doesn't exist. Exiting.")
    exit()

# Get OpenwWeather response
response = req.get(f"{BASE_URL}?q={CITY}&appid={API_KEY}&units=metric")
data = response.json()

# Tabulate format / headers variable
# Basic info
data_format_basic = [
    [
        data["name"],
        str(data["main"]["temp"]) + "°C",
        data["weather"][0]["description"].title(),
    ]
]
headers_basic = ["City", "Temperature", "Weather"]
# Detailed info
data_format_ext = [
    [
        data["name"],
        str(data["main"]["temp"]) + "°C",
        data["weather"][0]["description"].title(),
        str(data["main"]["feels_like"]) + "°C",
        str(data["main"]["humidity"]) + "%",
        str(data["main"]["pressure"]) + " hPa",
    ]
]
headers_ext = [
    "City",
    "Temperature (°C)",
    "Weather",
    "Feels-like",
    "Humidity",
    "Pressure",
]

if response.status_code == 200:
    print(tabulate(data_format_basic, headers=headers_basic, tablefmt="grid"))
    time.sleep(2)
    details = str(
        input(
            "Do you want to see further details? (perceived temp, humidity, pressure) [y/n] "
        )
    ).upper()
    if details == "Y" or details == "YES":
        # os.system('clear')
        print(tabulate(data_format_ext, headers=headers_ext, tablefmt="grid"))
        exit()
    elif details == "N" or details == "NO":
        print("Ok, have a great day!")
        exit()
    else:
        print("Error: Incorrect input provided!")
        exit()
else:
    print(f"Error fetching weather data, response code: {response.status_code}")
    exit()
    
