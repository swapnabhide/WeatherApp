import sys
sys.path.append("path/to/app")

import requests

from utils.get_geolocation import Geolocation
from utils.secrets import OPENWEATHER_API_KEY


def get_lon_lat_for_city(city_name):
    lat = Geolocation(city_name).get_latitude()
    lon = Geolocation(city_name).get_longitude()
    return lon, lat

def get_weather_by_city(city):
    """
    Not used as some smaller cities with larger cities with same name are not supported 
    """
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    return response.json()

def get_weather(city):
    lon, lat = get_lon_lat_for_city(city)
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"lon": lon, "lat": lat, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    return response.json()   


if __name__ == "__main__":
    city_name = input("Enter city name: ")

    print(get_weather_by_city(city = city_name))

    print("Weather by lon and lat \n\n")
    print(get_weather(city_name))