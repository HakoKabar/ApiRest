from django.shortcuts import render
from rest_framework import viewsets
from .models import Enterprise,Reservation
from .serializers import Enterprise_Serializer,Reservation_Serializer

class Enterprise_ViewSet(viewsets.ModelViewSet):
    queryset=Enterprise.objects.all()
    serializer_class=Enterprise_Serializer

class Reservation_ViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=Reservation_Serializer


