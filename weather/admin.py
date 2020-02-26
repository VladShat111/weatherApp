from django.contrib import admin
from .models import City
# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'sky', 'temperature',
                    'min_temperature', 'max_temperature', 'pressure',
                    'visibility', 'wind_speed', 'sunrise', 'sunset', 'date')
