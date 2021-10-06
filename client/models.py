from django.db import models
from django.db import models


class Client(models.Model):
    nom=models.CharField(max_length=10)
    prenom=models.CharField(max_length=10)
    telephone=models.IntegerField(default=0)
    email=models.CharField(max_length=30)