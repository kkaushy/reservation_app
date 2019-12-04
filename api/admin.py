from django.contrib import admin



from django.contrib.gis.admin import OSMGeoAdmin
from api.models import Category, ParkingSpot, Reservation


@admin.register(ParkingSpot)
class ParkingSpotAdmin(OSMGeoAdmin):
    list_display = ('description', 'category', 'is_active', 'location')


admin.site.register(Category)
admin.site.register(Reservation)

# Register your models here.
