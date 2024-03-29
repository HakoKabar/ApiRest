from django.db import models
from django.contrib.auth.models import User




class Enterprise(models.Model):
    NomE=models.CharField(max_length=20)
    TelephoneE=models.IntegerField()
    AdresseE=models.CharField(max_length=50)
    DescriptionE=models.CharField(max_length=200,null=True)

    def __str__(self) :
        return "%s" % (self.NomE)

class Reservation(models.Model):
    Nom_Client =models.ForeignKey(User,on_delete=models.CASCADE)
    Reseve_Par=models.ForeignKey(Enterprise,on_delete=models.CASCADE) 
    Type_De_Camion=models.IntegerField(choices=((1,'Break'),(2,'Forgon'),(3,'Camoin 20m'),(4,'Camion Poid Lourd'),(5,'Porteur')),default=0)
    Date_De_Debut_De_Reservation=models.DateField(null=False)
    Date_De_Fin_De_Reservation=models.DateField(null=False)

    class Meta :
        unique_together=(('Reseve_Par','Nom_Client'),)
        index_together =(('Reseve_Par','Nom_Client'),)

