
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
import random


def get_location(q):
    rand_no = int(random.random() * 100)
    geolocator = Nominatim(user_agent="ride_cell_test{}".format(rand_no))
    location = geolocator.geocode(q)
    user_location = Point(location.longitude, location.latitude, srid=4326)  
    return user_location