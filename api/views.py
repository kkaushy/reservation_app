from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.db.models import Count

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics

import json

from api.models import Category, ParkingSpot, Reservation
from api.serializers import CategorySerializer, ParkingSpotSerializer, ReservationSerializer
from api.utils import get_location


class ParkingSpotList(generics.ListCreateAPIView):
    def get_queryset(self):
        q = self.request.GET.get('q')
        radius = self.request.GET.get('radius')
        user_location = get_location(q)
        queryset = ParkingSpot.objects.filter(is_active=True).annotate(distance=Distance('location', user_location), reservation_count=Count('reservation')).filter(reservation_count=0)
        if radius:
            queryset = queryset.filter(distance__lt=radius)
        queryset = queryset.order_by('distance')
        return queryset
    serializer_class = ParkingSpotSerializer

class ParkingSpotDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        queryset = ParkingSpot.objects.all()        
        return queryset
    serializer_class = ParkingSpotSerializer


class ReservationList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Reservation.objects.all()        
        return queryset
    serializer_class = ReservationSerializer

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        queryset = Reservation.objects.all()        
        return queryset
    serializer_class = ReservationSerializer


class CategoryList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Category.objects.all()        
        return queryset
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        queryset = Category.objects.all()        
        return queryset
    serializer_class = CategorySerializer

