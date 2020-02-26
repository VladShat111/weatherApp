from django.shortcuts import render
from django.contrib import messages
import requests as r
from .models import City
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import CityFilter
# Create your views here.


def weather_api(request):

    if request.method == 'POST':
        city = request.POST.get('city')
        data = get_api_data(city)
        if 'message' not in data:
            try:
                city_name = data['name']
                counrty = data['sys']['country']
                sky = data['weather'][0]['main']
                description = data['weather'][0]['description']
                temp = data['main']['temp']
                min_temp = data['main']['temp_min']
                max_temp = data['main']['temp_max']
                pressure = data['main']['pressure']
                visibility = data['visibility']
                wind_speed = data['wind']['speed']
                sunrise = data['sys']['sunrise']
                sunset = data['sys']['sunset']
            except KeyError as e:
                print(e)
                messages.warning(request, 'Something goes wrong!!!')
                return render(request, 'app/weather/find_city.html')

            # if City.objects.filter(name=city_name).exists():
            #     City.objects.filter(name=city_name).update(country=counrty, sky=sky, description=description,
            #                                                temperature=temp, min_temperature=min_temp, max_temperature=max_temp,
            #                                                pressure=pressure, visibility=visibility, wind_speed=wind_speed,
            #                                                sunrise=sunrise, sunset=sunset, date=timezone.now())
            # else:
            City.objects.create(name=city_name, country=counrty, sky=sky, description=description, temperature=temp,
                                min_temperature=min_temp, max_temperature=max_temp, pressure=pressure,
                                visibility=visibility, wind_speed=wind_speed, sunrise=sunrise, sunset=sunset)

            messages.success(request, f'In {city_name} the weather is {description}, sky is {sky}, temperature is {temp},'
            f' pressure is {pressure}, visibility is {visibility}, wind speed is {wind_speed},'
            f' sunrise and sunset is {sunrise}, {sunset} respectively')

            return render(request, 'app/weather/find_city.html')

        messages.warning(request, f"The '{city}' is not valid. Try again!")
        return render(request, 'app/weather/find_city.html')

    return render(request, 'app/weather/find_city.html', {'City': City.objects.all()})


def list_of_city(request):
    my_filter = CityFilter(request.GET, queryset=City.objects.all().order_by('-pk'))
    paginator = Paginator(my_filter.qs, 2)

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {'cities': page_obj,
               'my_filter': my_filter}

    return render(request, 'app/weather/city_list.html', context)


def get_api_data(city):
    return r.get(url='http://api.openweathermap.org/data/2.5/weather?q=' + city +'&APPID=1af0e3be0200a196516ae6050fcb9212').json()