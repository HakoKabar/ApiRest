
from django import urls
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cleint/',include('client.urls')),
    path('entreprise/',include('enterprise.urls')),
    

]
