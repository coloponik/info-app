import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    return render(request, 'weather/index.html')
    
def weather(request):

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    
    if cities:
        appid = "02f77820f95bde53f1fad1edae3d923d"
        all_cities = []
        try:
            for city in cities:
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                params={'q': city.name, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                data = res.json()
                city_info = {
                    'city': city.name,
                    'descrip': data['weather'][0]['description'],
                    'temp': data['main']['temp'],
                    'hum': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'icon': data['weather'][0]['icon']
                }
                all_cities += [city_info]
            context = {'info': all_cities, 'form': form}
        except Exception:
            print('\n  Нет информации о данном городе.')

    return render(request, 'weather/weather.html', context)