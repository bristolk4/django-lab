from django.urls import path
from . import views

urlpatterns = [
    path('api/location', views.LocationList.as_view(), name='location_list'), 
    path('api/location/<int:pk>', views.LocationDetail.as_view(), name='location_detail'),
]