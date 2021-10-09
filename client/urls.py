
from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import ClientViewSet,ReservationViewSet

RouterClient=routers.DefaultRouter()
RouterClient.register('client',ClientViewSet)
RouterClient.register('reservation',ReservationViewSet)




urlpatterns = [
    
    path('',include(RouterClient.urls)),
    
    
    
    
]
