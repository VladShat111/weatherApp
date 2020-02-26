from django.urls import path
from .views import list_of_city, weather_api

urlpatterns = [
    path('find/', weather_api, name='find'),
    path('cities/', list_of_city, name='cities'),
]