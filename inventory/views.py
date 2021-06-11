from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Consumable,Location,LocationConsumable,Course
from .serializers import ConsumableSerializer,LocationSerializer,LocationConsumableSerializer,CourseSerializer,MovementEntrySerializer,MovementExitSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

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

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EntryMovementView(APIView):
    serializer_class = MovementEntrySerializer
    def post(self, request, format=None):
        data = request.data
        serializer = MovementEntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)
        import pdb; pdb.set_trace()

class ExitMovementView(APIView):
    serializer_class = MovementExitSerializer
# Create your views here.
