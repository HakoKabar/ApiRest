from rest_framework import routers

from enterprise.views import Enterprise_ViewSet, Reservation_ViewSet
from django.urls import path,include

router=routers.DefaultRouter()
router.register('enterprise',Enterprise_ViewSet)
router.register('reservation',Reservation_ViewSet)

urlpatterns = [
    
    path('',include(router.urls)),
    
    
    
]

