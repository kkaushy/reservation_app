
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim



def get_location(q):
    geolocator = Nominatim(user_agent="ride_cell_test")
    location = geolocator.geocode(q)
    user_location = Point(location.longitude, location.latitude, srid=4326)  
    return user_location