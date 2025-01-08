from django.urls import path
from . import views

urlpatterns = [
    path('api/company', views.CompanyList.as_view(), name='company'), 
    path('api/company/<int:pk>', views.CompanyDetail.as_view(), name='company'),
]