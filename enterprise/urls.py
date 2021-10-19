from rest_framework import routers

from enterprise.views import Enterprise_ViewSet, Reservation_ViewSet
from django.urls import path,include

router=routers.DefaultRouter()
router.register('enter',Enterprise_ViewSet)
router.register('reser',Reservation_ViewSet)


urlpatterns = [
    
    path('',include(router.urls)),


    
]

