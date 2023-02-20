import requests
import json

from get_geolocation import Geolocation
from utils.secrets import OPENWEATHER_API_KEY

city_name = input("Enter city name: ")

lat = Geolocation(city_name).get_latitude()
lon = Geolocation(city_name).get_longitude()

# Constructing the API URL path
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={OPENWEATHER_API_KEY}"

response = requests.get(url)

res = response.json()
main = res["main"]
weather = res["weather"][0]

# TODO: build a UI
print(f"Right now in {res['name']} is {main['temp']}.")
if res["main"]["temp"] != res["main"]["feels_like"]:
    print(f"It feels like {main['feels_like']}")
print(f"There will be {weather['main']}") ## TODO: add some logic here. What other values can we get?
print(f"Forcasted high of {main['temp_max']} C and low of {main['temp_min']} C"
)