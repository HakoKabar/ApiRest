from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices, TextChoices
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey


class Client(models.Model):
    nom=models.CharField(max_length=10)
    prenom=models.CharField(max_length=10)
    telephone=models.IntegerField(default=0)
    email=models.CharField(max_length=50)
    def __str__(self) :
        return "%s %s" % (self.nom, self.prenom)


class Reservation(models.Model):
    ReservationClient=ForeignKey(Client,on_delete=CASCADE) 
    TypeDeCamion=IntegerField(choices=((1,'Break'),(2,'Forgon'),(3,'Camoin 20m'),(4,'Camion Poid Lourd'),(5,'Porteur')),default=0)

