from rest_framework import serializers
from .models import Consumable,Location,LocationConsumable,Entry,Course,Exit,Order

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

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['count','date','part_number','purchase_order','lot','owner','date_shelflife','quantity']

class ExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exit
        fields = ['count','date','order','owner','lot','user_deliver','observations']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['count','date','order','lot','course_code','course_number','quantity','user_requesting','status']

   
  