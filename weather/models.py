from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    sky = models.CharField(max_length=50, blank=True)
    temperature = models.IntegerField(default=0, blank=True)
    min_temperature = models.IntegerField(default=0, blank=True)
    max_temperature = models.IntegerField(default=0, blank=True)
    pressure = models.IntegerField(default=0, blank=True)
    visibility = models.IntegerField(default=0, blank=True)
    wind_speed = models.IntegerField(default=0, blank=True)
    sunrise = models.IntegerField(default=0, blank=True)
    sunset = models.IntegerField(default=0, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
