from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
import json

from api.models import Category, ParkingSpot, Reservation
from api.serializers import CategorySerializer, ParkingSpotSerializer, ReservationSerializer


class LocationView(APIView):

    def get(self, request):
        
        response = {
            'results': "data",
        }        
        return JsonResponse(response, safe=False)





class ParkingSpotList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = ParkingSpot.objects.all()        
        return queryset
    serializer_class = ParkingSpotSerializer
    # permission_classes = ( IsAuthenticated, )

class ParkingSpotDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        queryset = ParkingSpot.objects.all()        
        return queryset
    serializer_class = ParkingSpotSerializer
    # permission_classes = ( IsAuthenticated, )







class ReservationList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Reservation.objects.all()        
        return queryset
    serializer_class = ReservationSerializer
    # permission_classes = ( IsAuthenticated, )

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        queryset = Reservation.objects.all()        
        return queryset
    serializer_class = ReservationSerializer
    # permission_classes = ( IsAuthenticated, )







class CategoryList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Category.objects.all()        
        return queryset
    serializer_class = CategorySerializer
    # permission_classes = ( IsAuthenticated, )

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        queryset = Category.objects.all()        
        return queryset
    serializer_class = CategorySerializer
    # permission_classes = ( IsAuthenticated, )
