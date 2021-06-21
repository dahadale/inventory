from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Consumable,Location,LocationConsumable,Course,Requisition,Exit,Entry
from .serializers import ConsumableSerializer,LocationSerializer,LocationConsumableSerializer,CourseSerializer,EntrySerializer,ExitSerializer,RequisitionSerializer
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

class EntryView(APIView):
    serializer_class = EntrySerializer
    def post(self, request, format=None):
        data = request.data
        serializer = EntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)
        import pdb; pdb.set_trace()

class RequisitionList(generics.ListCreateAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer


class ExitList(generics.ListCreateAPIView):
    queryset = Exit.objects.all()
    serializer_class = ExitSerializer