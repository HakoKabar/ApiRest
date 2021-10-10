
from django.shortcuts import render
from rest_framework import viewsets,status,request
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
            username =request.data['username']
            user=User.objects.get(username=username)
            Reseve_Par= Enterprise.objects.get(id=pk)

            Type_De_Camion=request.data['Type_De_Camion']
            Date_De_Debut_De_Reservation=request.data['Date_De_Debut_De_Reservation']
            Date_De_Fin_De_Reservation=request.data['Date_De_Fin_De_Reservation']
            try:
                reser=Reservation.objects.get(Nom_Client=user.id,Reseve_Par=Reseve_Par.id)
                reser.Type_De_Camion=Type_De_Camion
                reser.Date_De_Debut_De_Reservation=Date_De_Debut_De_Reservation
                reser.Date_De_Fin_De_Reservation=Date_De_Fin_De_Reservation
                reser.save()
                Serialization= Reservation_Serializer(reser,many=False)
                 
                json = {
                 'Methode utlise ': 'Updata',
                 
                 }
                return Response(json, Serialization.data)
            except:
                
                reser=Reservation.objects.create(Nom_Client=user,Reseve_Par=Reseve_Par,
                Type_De_Camion=Type_De_Camion,Date_De_Debut_De_Reservation=Date_De_Debut_De_Reservation,
                Date_De_Fin_De_Reservation=Date_De_Fin_De_Reservation)
                Serialization= Reservation_Serializer(reser,many=False)
                json = {
                 'Reserve par ':Reseve_Par.id,
                 'Userr':user,
                 'Camion':Type_De_Camion,
                 'dateD' :Date_De_Debut_De_Reservation,
                 'dateF' :Date_De_Fin_De_Reservation,
                 'Methode utlise ': 'CreateErreur',
                 'result':Serialization.data
                
                 }
                
            return Response(json ,status=status.HTTP_400_BAD_REQUEST)

        else :
        
            json = {
            'Methode utlise ': 'Erreur'
            }
        return Response(json , status=status.HTTP_400_BAD_REQUEST)

class Reservation_ViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=Reservation_Serializer


