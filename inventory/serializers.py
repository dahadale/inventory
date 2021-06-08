from rest_framework import serializers
from .models import Consumable,Location,LocationConsumable

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