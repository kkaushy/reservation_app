from django.conf import settings
from rest_framework import serializers

from api.models import Category, ParkingSpot, Reservation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'cost', 'createdAt', 'updatedAt')
        read_only_fields = ('id',)


class ParkingSpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingSpot
        fields = ('id', 'location', 'description', 'category', 'is_active', 'createdAt', 'updatedAt')
        read_only_fields = ('id',)



class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ('id', 'description', 'parking_spot', 'duration', 'is_active', 'createdAt', 'updatedAt')
        read_only_fields = ('id',)
