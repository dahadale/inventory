from django.urls import include, path
from .views import ConsumableList,LocationList,LocationConsumableList

urlpatterns = [
    path('consumables/', ConsumableList.as_view(),name='consumables'),
    path('locations/', LocationList.as_view(),name='locations'),
    path('location/consumables/', LocationConsumableList.as_view(),name='location-consumables')
]