from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from .models import *
from django.http import HttpResponse
import datetime
from geopy.distance import distance as geo_distance
import requests
import json


def find_closest_city(lat, long, distance=20, model_type='current'):
    ''' 
    find a the city data for "type" (current or prediction) that's 
    "distance" kilometers away from
    existing city in db if it exists
    '''
    if model_type == 'current':
        queryset = GlobalCurrent.objects.all()
    else:
        queryset = GlobalPredict.objects.all()
    
    found_closest = False # closest city within certain limit exists in db
    # min_distance = 
    # for city in queryset:



def get_global_current(lat, long):
    pass

def get_global_predict(lat, long):
    pass

class GlobalCurrentView(generics.RetrieveAPIView):

    pass

class GlobalPredictView(generics.RetrieveAPIView):
    pass











# function to scrape current weather data if 1 hours has passed since last update_time 
def domestic_initial_scrape(delay=1):
    # 한국 표준시간
    KST = datetime.timezone(datetime.timedelta(hours=9))
    # check whether scrapped in the last 12 hours
    sample_city = DomesticCurrent.objects.get(id=1)
    curr_time = datetime.datetime.now(tz=KST)
    delta = datetime.timedelta(hours=delay)
    # just return without updating if less than 1 hour has passed since last update
    if curr_time - sample_city.update_time < delta:
        return

    # scraping and update part
    curr_wea = requests.get(
        'http://www.weather.go.kr/weather/observation/currentweather.jsp')
    current = BeautifulSoup(curr_wea.content, 'html.parser')
    
    # get the weather table
    table = current.find_all("tbody")
    
    # get all entries for the table, 94 cities
    entries = table[0].find_all("tr")

    # data columns that i care about
    valid_columns = [1, 5, 7, 8, 9, 10, 11]
    for city_idx in range(len(entries)):
        # data for each city in table
        city_data = entries[city_idx].find_all("td")
        curr_city, bool_created = CurrentWeather.objects.get_or_create(
            id=city_idx+1, location=city_data[0].text)
        cleaned_data = [city_data[idx].text if city_data[idx].text !=
                        '\xa0' else None for idx in valid_columns]
        curr_city.status, curr_city.temp, curr_city.windchill, curr_city.rain, curr_city.snow, curr_city.humidity, curr_city.wind_direction = cleaned_data
        curr_city.save()



class DomesticCurrentView(generics.ListAPIView):
    queryset = DomesticCurrent.objects.all()
    serializer_class = DomesticCurrentSerializer

    def list(self, request):
        domestic_initial_scrape()
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = DomesticCurrentSerializer(queryset, many=True)
        return Response(serializer.data)


# class ShortPredictionWeatherView(generics.ListAPIView):
#     queryset = ShortPredictionWeather.objects.all()
#     serializer_class = ShortPredictionWeatherSerializer
