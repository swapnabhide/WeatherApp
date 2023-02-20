# Get Langitude and Longitude of a location

from geopy.geocoders import Nominatim

from utils.exceptions import LocationError

class Geolocation:
    def __init__(self, city, state=None, country=None):
        if state is not None:
            self.location = Nominatim(user_agent="WeatherApp").geocode(f'{city},{state},{country}')
        elif country is not None:
            self.location = Nominatim(user_agent="WeatherApp").geocode(f'{city},{country}')
        else:
            self.location = Nominatim(user_agent="WeatherApp").geocode(city)

        if self.location is None:
            raise LocationError(f"{city}, {state}, {country}")

    def get_latitude(self):
        return self.location.latitude

    def get_longitude(self):
        return self.location.longitude


if __name__ == "__main__":
    pune_location = Geolocation('Pune')
    print(f"Pune is at {pune_location.get_latitude()} latitude and {pune_location.get_longitude()} longitude")

    location = Geolocation('Newton', 'Massachusetts', 'USA')
    print(f"Newton, Massachusetts is at {location.get_latitude()} latitude and {location.get_longitude()} longitude")

    location = Geolocation(city='Edinburgh', country='UK')
    print(f"Edinburgh, UK is at {location.get_latitude()} latitude and {location.get_longitude()} longitude")

    try:
        invalid_location = Geolocation(city="minas morghul")
        print(invalid_location.get_latitude())
    except LocationError as le:
        print(f" Caught excaption {repr(le)}")
