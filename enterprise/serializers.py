from django.db.models import fields
from rest_framework import serializers
from .models import Enterprise,Reservation


class Enterprise_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Enterprise
        fields=('id','NomE','TelephoneE','AdresseE','DescriptionE','nbr_de_reservation','moyen_de_camion')

class Reservation_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Reservation
        fields='__all__'