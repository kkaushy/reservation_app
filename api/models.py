# from django.db import models
from django.contrib.gis.db import models


class Category(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    cost = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ParkingSpot(models.Model):
    class Meta:
        ordering = ['updatedAt',]      
    # longitude = models.FloatField()
    # latitude = models.FloatField()   
    location = models.PointField(null=True, blank=True) 
    description = models.CharField(max_length=255,blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    



class Reservation(models.Model):
    class Meta:
        ordering = ['updatedAt',]

    description = models.CharField(max_length=255,blank=True, null=True)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    duration = models.IntegerField()
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)    