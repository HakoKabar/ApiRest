from django.db.models import fields
from rest_framework import serializers
from .models import Enterprise,Reservation


class Enterprise_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Enterprise
        fields='__all__'

class Reservation_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Reservation
        fields='__all__'