from django.urls import include, path
from .views import ConsumableList,LocationList,LocationConsumableList,EntryView,RequisitionList,ExitList

urlpatterns = [
    path('consumables/', ConsumableList.as_view(),name='consumables'),
    path('locations/', LocationList.as_view(),name='locations'),
    path('location/consumables/', LocationConsumableList.as_view(),name='location-consumables'),
    path('entry/', EntryView.as_view(),name='entry'),
    path('requisition/', RequisitionList.as_view(),name='requisition'),
    path('exit/', ExitList.as_view(),name='exit')
]