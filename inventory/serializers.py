from rest_framework import serializers
from .models import Consumable,Location,LocationConsumable,Movement,Course

class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumable
        fields = ['part_number', 'item_name', 'fsc', 'niin', 'unit_price','unit_issue','shelf_life']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['code','description']



class LocationConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationConsumable
        fields = ['consumable','location']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['code','name','description']

class MovementEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = ['movement_type','date','consumable','purchase_order','lot','owner','date_shelflife','quantity']

class MovementExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = ['movement_type','date','consumable','purchase_order','lot','owner','date_shelflife','quantity']