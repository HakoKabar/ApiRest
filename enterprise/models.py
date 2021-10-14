from django.db import models
from django.contrib.auth.models import User

#-----------------Import pour auto Token-------------------------
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
#----------------------------------------------------------------




class Enterprise(models.Model):
    NomE=models.CharField(max_length=20)
    TelephoneE=models.IntegerField()
    AdresseE=models.CharField(max_length=50)
    DescriptionE=models.CharField(max_length=200,null=True)

    def __str__(self) :
        return "%s" % (self.NomE)

    #-----------------Compte les Nombre de reservation effectue par  chaque Eentreprise------------------------------------------------

    def nbr_de_reservation(self):
        nbr=Reservation.objects.filter(Reseve_Par=self)
        if len(nbr) > 0:
            return len(nbr)
        else :
            return 0
    
    #----------------------------------------------------------------------------------------------------
    def Liste_de_camion(self):
        nbr=Reservation.objects.filter(Reseve_Par=self)
        lis=[]
        for x in nbr :
           lis.append(x.Type_De_Camion)

        return lis
        

class Reservation(models.Model):
    Nom_Client =models.ForeignKey(User,on_delete=models.CASCADE)
    Reseve_Par=models.ForeignKey(Enterprise,on_delete=models.CASCADE) 
    Type_De_Camion=models.IntegerField(default=0)


 
    class Meta :
        unique_together=(('Reseve_Par','Nom_Client'),)
        index_together =(('Reseve_Par','Nom_Client'),)

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance,created, **kwargs):
    if created :
        Token.objects.create(user = instance)