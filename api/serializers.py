from django.conf import settings
from rest_framework import serializers

from api.models import Category, ParkingSpot, Reservation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'cost', 'createdAt', 'updatedAt')
        read_only_fields = ('id',)


class ParkingSpotSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name', default="")
    category_cost = serializers.ReadOnlyField(source='category.cost', default="")
    class Meta:
        model = ParkingSpot
        fields = ('id', 'location', 'description', 'category', 'is_active', 'category_name','category_cost', 'createdAt', 'updatedAt')
        read_only_fields = ('id',)


class ReservationSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='parking_spot.category.name', default="")
    category_cost = serializers.ReadOnlyField(source='parking_spot.category.cost', default="")
    parking_spot_description = serializers.ReadOnlyField(source='parking_spot.description', default="")
    class Meta:
        model = Reservation
        fields = ('id', 'description', 'parking_spot', 'duration', 'is_active', 'category_name', 'category_cost', 'parking_spot_description', 'createdAt', 'updatedAt')
        read_only_fields = ('id',)
