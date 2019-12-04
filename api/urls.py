"""reservation_app URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from api.views import ParkingSpotList, ParkingSpotDetail, ReservationList, ReservationDetail, CategoryList, CategoryDetail

urlpatterns = [    

    path(r'parkingspot/', ParkingSpotList.as_view()),
    path(r'parkingspot/<int:pk>/', ParkingSpotDetail.as_view()),    

    path(r'reservation/', ReservationList.as_view()),
    path(r'reservation/<int:pk>/', ReservationDetail.as_view()),    

    path(r'category/', CategoryList.as_view()),
    path(r'category/<int:pk>/', CategoryDetail.as_view()),   

]
