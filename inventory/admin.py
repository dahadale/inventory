from django.contrib import admin

from .models import Consumable,Movement,Owner,Location,LocationConsumable,Course


@admin.register(Consumable)
class ConsumableAdmin(admin.ModelAdmin):
    list_display = [
         'part_number','item_name','fsc','niin','unit_price','unit_issue','shelf_life'
           ]
    search_fields = ['part_number']
    

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ['movement_type', 'date', 'consumable']
    raw_id_fields = ['consumable']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['code','name']
    search_fields = ['code']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['code','description']
    search_fields = ['code']

@admin.register(LocationConsumable)
class LocationConsumableAdmin(admin.ModelAdmin):
    list_display = ['consumable','location']
    raw_id_fields = ['consumable','location']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code','name','description']
    search_fields = ['code']

# Register your models here.


