from rest_framework import routers


from django.urls import path

from .views import index

urlpatterns = [
    
    

    path('',index),
    
]