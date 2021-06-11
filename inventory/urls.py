from django.urls import include, path
from .views import ConsumableList,LocationList,LocationConsumableList,EntryMovementView

urlpatterns = [
    path('consumables/', ConsumableList.as_view(),name='consumables'),
    path('locations/', LocationList.as_view(),name='locations'),
    path('location/consumables/', LocationConsumableList.as_view(),name='location-consumables'),
    path('movements/entry/', EntryMovementView.as_view(),name='movements-entry')
]