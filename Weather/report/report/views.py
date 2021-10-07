from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def index(request):
    return render(request,'index.html')

def weather(request):
   

    city=request.GET.get('city','default')
    namel=request.GET.get('myname','default')
    print(city)
    print(namel)
    mainurl="http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f17064a6d66ca1a76a898a31680cfa0a"

    r=requests.get(mainurl)
    r=r.json()
    kel=r['main']['temp']
    Tc=kel-273.15
    f= int(Tc)
    city_weather={
        'name':namel,
        'city':city,
        'temperature':f,
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
    }
    if r['weather'][0]['description']=='rain':
        return render(request,'rain.html',city_weather)

    f=r['weather'][0]['description']
    stud=f.split()
    for i in stud:
        if i=='rain':
            return render(request,'rain.html',city_weather)

    for i in stud:
        if i=='clouds':
            return render(request,'cloud.html',city_weather)

    for i in stud:
        if i=='smoke':
             return render(request,'smoke.html',city_weather)


    print(stud)       



    if city=='delhi':
         return render(request,'delhi.html',city_weather)
            
    
    else:
        return render(request,'weather.html',city_weather)


    
  
def details(request):
    return render(request,'details.html') 

def contact(request):
    return render(request,'contactus.html')    

def city(request):
    kent=list('delhi','mumbai','chennai','bengaluru')
    for i in kent:
        mainurl="http://api.openweathermap.org/data/2.5/weather?q=" + i + "&appid=f17064a6d66ca1a76a898a31680cfa0a"
        r=requests.get(mainurl)
        r=r.json()
        kel=r['main']['temp']
        Tc=kel-273.15
        f= int(Tc)
        city_weather={
        
        
        'temperature':f,
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon']
        }

    return render(request,'city.html')

