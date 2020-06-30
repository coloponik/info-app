import requests
from datetime import datetime
from django.utils import timezone
import time 
from django.shortcuts import render
from .models import City
from .forms import CityForm

def reqApi(city):
    try:
        appid = "02f77820f95bde53f1fad1edae3d923d"
        # appid = "f65749c1cb61cf824f936ed96ffd763b"
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
        params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        return data
    except Exception:
        print("Что-то пошло не так...")

    # req_info = {
    #     'city': city,
    #     'descrip': data['weather'][0]['description'],
    #     'temp': data['main']['temp'],
    #     'hum': data['main']['humidity'],
    #     'pressure': data['main']['pressure'],
    #     'icon': data['weather'][0]['icon']
    # }

def weather(request):
    # cities = City.objects.all()

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        city = request.POST.get("name")
        data = reqApi(city)
        if data:
            city_info = {
                'city': city,
                'descrip': data['weather'][0]['description'],
                'temp': data['main']['temp'],
                'hum': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'icon': data['weather'][0]['icon']
            }
            context = {'info': city_info, 'form': form}
            return render(request, 'weather/weather.html', context)
    else:
        form = CityForm()
        context = {'form': form}
        return render(request, 'weather/weather.html', context)

    # if cities:
    #     all_cities = []
    #     for city in cities:
    #         now = timezone.now()
    #         then = city.time
    #         now_ts = time.mktime(now.timetuple())
    #         then_ts = time.mktime(then.timetuple())
    #         delta = abs(int(then_ts - now_ts) / 60)
    #         if delta > 1.0 or city.descrip == '':
    #             city_info = reqApi(city.name)
    #             new_city_info = Person.objects.get_or_create(name=city_info.city, descrip=city_info.descrip, temp=city_info.temp, hum=city_info.hum, pressure=city_info.pressure, icon=city_info.icon, time=datetime.now())
    #         else:
    #             city_info = {
    #                 'city': city.name,
    #                 'descrip': city.descrip,
    #                 'temp': city.temp,
    #                 'hum': city.hum,
    #                 'pressure': city.pressure,
    #                 'icon': city.icon
    #             }
    #         all_cities += [city_info]
    #     context = {'info': all_cities, 'form': form}
    #     return render(request, 'weather/weather.html', context)
    # else:
    #     context = {'form': form}
    #     return render(request, 'weather/weather.html', context)



    #     res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    #     params={'q': city.name, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    #     data = res.json()
    #     city_info = {
    #         'city': city.name,
    #         'descrip': data['weather'][0]['description'],
    #         'temp': data['main']['temp'],
    #         'hum': data['main']['humidity'],
    #         'pressure': data['main']['pressure'],
    #         'icon': data['weather'][0]['icon']
    #     }
