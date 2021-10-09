from django.shortcuts import render
from .models import Client,Reservation
from .serializers import ClientSerializer,ReservationSerailizer
from rest_framework import viewsets,permissions

class  ClientViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer
    permission_classes=[permissions.IsAuthenticated,]
    filterset_fields=['nom','prenom']
    search_fields=['nom','prenom']

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerailizer

    
