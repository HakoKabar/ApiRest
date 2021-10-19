from django.shortcuts import render
import json
import urllib.request
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

@csrf_exempt
def index(request):
    if request.method == 'POST':
       
        city=request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + 
                                        city + '&units=metric&appid=c739777f94bf043f409980780b688ce2').read()
                                      
        
        list_of_data=json.loads(source)
        data={
            "country" :  str(list_of_data['sys']['country']),
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
        }
        print(data)
    else  :
        data ={}

    return render(request,"fond/index.html",data)