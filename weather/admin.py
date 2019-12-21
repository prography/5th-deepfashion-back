from django.contrib import admin

# Register your models here.

from .models import *



admin.site.register(CurrentWeather)
admin.site.register(ShortPredictionWeather)
