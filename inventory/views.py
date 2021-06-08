from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Consumable,Location,LocationConsumable
from .serializers import ConsumableSerializer,LocationSerializer,LocationConsumableSerializer

class ConsumableList(generics.ListCreateAPIView):
    queryset = Consumable.objects.all()
    serializer_class = ConsumableSerializer

    # permission_classes = [IsAdminUser]

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationConsumableList(generics.ListCreateAPIView):
    queryset = LocationConsumable.objects.all()
    serializer_class = LocationConsumableSerializer
# Create your views here.
