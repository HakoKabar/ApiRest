
from django.shortcuts import render
from rest_framework import serializers, viewsets,status,request
from .models import Enterprise,Reservation
from .serializers import Enterprise_Serializer,Reservation_Serializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User





class Enterprise_ViewSet(viewsets.ModelViewSet):
   
    queryset=Enterprise.objects.all()
    serializer_class=Enterprise_Serializer

    @action(detail=True, methods=['post'])
    def entreprise_reservation(self,request,pk=None):
        if 'Type_De_Camion' in request.data :
            nom =request.data['nom']
            Nom_Client=User.objects.get(username=nom)
            Socite= Enterprise.objects.get(id=pk)
            Type_De_Camion=request.data['Type_De_Camion']
            
            try:
                reser=Reservation.objects.get(Nom_Client=Nom_Client.id,Reseve_Par=Socite.id)
                reser.Type_De_Camion=Type_De_Camion
                reser.save()
                Serialization= Reservation_Serializer(reser,many=False)
                json = {
                 'user':nom,
                 'socite':Socite.id,
                 'Camion':Type_De_Camion,

                 'Methode utlise ': 'Updata',
                 'result':Serialization.data
                 
                }
                return Response(json, status=status.HTTP_400_BAD_REQUEST)
            except:
                
                reser=Reservation.objects.create(Nom_Client=Nom_Client,Reseve_Par=Socite,Type_De_Camion=Type_De_Camion)
                Serialization= Reservation_Serializer(reser,many=False)
                json = {
                 'Methode utlise ': 'CreateErreur',
                 'result':Serialization.data
                
                }
                
                return Response(json,status=status.HTTP_200_OK)

        else :
        
            json = {
            'Methode utlise ': 'Erreur'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)

class Reservation_ViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=Reservation_Serializer

