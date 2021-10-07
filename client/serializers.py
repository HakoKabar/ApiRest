from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Client,Reservation

class ClientSerializer(serializers.ModelSerializer):
    class Meta :
        model = Client
        fields ='__all__'
class ReservationSerailizer(serializers.ModelSerializer):
    class Meta :
        model = Reservation
        fields='__all__'