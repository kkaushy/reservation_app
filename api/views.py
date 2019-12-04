from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
import json

from api.models import Category, ParkingSpot, Reservation
from api.serializers import CategorySerializer, ParkingSpotSerializer, ReservationSerializer
from api.utils import get_location



from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance





class LocationView(APIView):

    def get(self, request):
        
        longitude = 72.9097417560117
        latitude = 18.91391780695173


        user_location = Point(longitude, latitude, srid=4326)   
        import pdb;pdb.set_trace()
        ps_list = ParkingSpot.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:6]
        # for ps in ps_list:
        response = {
            'results': "data",
        }        
        return JsonResponse(response, safe=False)





class ParkingSpotList(generics.ListCreateAPIView):
    def get_queryset(self):
        q = self.request.GET.get('q')
        radius = self.request.GET.get('radius')
        user_location = get_location(q)
        queryset = ParkingSpot.objects.filter(is_active=True).annotate(distance=Distance('location', user_location))
        if radius:
            queryset = queryset.filter(distance__lt=radius)
        queryset = queryset.order_by('distance')
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
