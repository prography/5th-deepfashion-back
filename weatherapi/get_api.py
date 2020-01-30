# python file for helper files that contain functions to communicate with APIs

from .models import *
import datetime
from geopy.distance import distance as geo_distance
from bs4 import BeautifulSoup
import requests
import json
import datetime
import decouple
WEATHER_API_KEY = decouple.config("WEATHER_API_KEY")


def find_closest_city(lat, long, acceptable_distance=15, model_type='current'):
    ''' 
    find a the city data for "type" (current or predict) that's 
    "distance" kilometers away from
    existing city in db if it exists
    return city id of closest city within acceptable_distance
    '''
    if model_type == 'current':
        queryset = InternationalCurrent.objects.all()
    else:
        queryset = GlobalPredict.objects.all()

    min_distance = acceptable_distance + 1
    origin_coordinates = (lat, long)
    city_id = None
    # find min distance
    for city in queryset:
        distance = geo_distance(
            origin_coordinates, (city.latitude, city.longitude))
        if distance < min_distance:
            min_distance = distance
            city_id = city.city_id
    return city_id


def clean_names_current(json_dict):
    '''
    funtion to take in parsed json data in python dict form and rename keys to fit InternationalCurrent model
    '''
    transformed_dict = dict()
    transformed_dict['latitude'] = json_dict['coord']['lat']
    transformed_dict['longitude'] = json_dict['coord']['lon']
    transformed_dict['weather_id'] = json_dict['weather'][0]['id']
    transformed_dict['weather_main'] = json_dict['weather'][0]['main']
    transformed_dict['weather_description'] = json_dict['weather'][0]['description']
    transformed_dict['weather_icon'] = json_dict['weather'][0]['icon']
    transformed_dict['temperature'] = json_dict['main']['temp']
    transformed_dict['feels_like'] = json_dict['main']['feels_like']
    transformed_dict['pressure'] = json_dict['main']['pressure']
    transformed_dict['humidity'] = json_dict['main']['humidity']
    transformed_dict['wind_speed'] = json_dict['wind']['speed']
    transformed_dict['wind_direction'] = json_dict['wind']['deg']

    transformed_dict['cloud'] = json_dict['clouds']['all']
    if 'rain' in json_dict:
        if '1h' in json_dict['rain']:
            transformed_dict['rain_one_hour'] = json_dict['rain']['1h']
        if '3h' in json_dict['rain']:
            transformed_dict['rain_three_hour'] = json_dict['rain']['3h']
    if 'snow' in json_dict:
        if '1h' in json_dict['snow']:
            transformed_dict['snow_one_hour'] = json_dict['snow']['1h']
        if '3h' in json_dict['snow']:
            transformed_dict['snow_three_hour'] = json_dict['snow']['3h']

    new_datetime = datetime.datetime.fromtimestamp(json_dict['dt'])
    transformed_dict['calculation_datatime'] = new_datetime
    transformed_dict['city_country'] = json_dict['sys']['country']
    transformed_dict['city_id'] = int(json_dict['id'])
    transformed_dict['city_name'] = json_dict['name']
    return transformed_dict


def clean_names_predict(json_dict):
    cleaned_data = dict()
    cleaned_data['latitude'] = json_dict['city']['coord']['lat']
    cleaned_data['longitude'] = json_dict['city']['coord']['lon']
    cleaned_data['city_id'] = json_dict['city']['id']
    cleaned_data['data'] = json_dict['list']
    return cleaned_data


def get_create_current_weather(lat, long, api_key=WEATHER_API_KEY, delay=1):
    '''
    Get or create current/predict weather data from api
    '''
    current_id = "http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&appid={api_key}"
    current_lat_long = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=metric&appid={api_key}"
    KST = datetime.timezone(datetime.timedelta(hours=9))
    closest_city_id = find_closest_city(lat, long, model_type='current')
    curr_time = datetime.datetime.now(tz=KST)
    delta = datetime.timedelta(hours=delay)

    if closest_city_id != None:
        closest_city = InternationalCurrent.objects.get(
            city_id=closest_city_id)
        if curr_time - closest_city.updated_time < delta:
            # data is less than one hour old
            return closest_city
        else:
            # data is more than one hour old
            json_data = requests.get(current_id.format(
                city_id=closest_city_id, api_key=WEATHER_API_KEY))
            json_dict = json.loads(json_data.text)
            cleaned_data = clean_names_current(json_dict)
            # update date or make new data
            closest_city, bool_created = InternationalCurrent.objects.update_or_create(
                city_id=cleaned_data['city_id'], defaults=cleaned_data)
            return closest_city
    else:  # if closest city ID is None:
        json_data = requests.get(current_lat_long.format(
            lat=lat, long=long, api_key=WEATHER_API_KEY))
        json_dict = json.loads(json_data.text)
        cleaned_data = clean_names_current(json_dict)
        # update or create city weather data
        # breakpoint()
        closest_city, bool_created = InternationalCurrent.objects.update_or_create(
            city_id=cleaned_data['city_id'], defaults=cleaned_data)
        return closest_city


def get_create_predict_weather(lat, long, api_key=WEATHER_API_KEY, delay=1):
    '''
    Get or create current/predict weather data from api
    '''
    predict_id = "https://api.openweathermap.org/data/2.5/forecast?id={city_id}&units=metric&cnt=8&appid={api_key}"
    predict_lat_long = "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&units=metric&cnt=8&appid={api_key}"
    KST = datetime.timezone(datetime.timedelta(hours=9))
    closest_city_id = find_closest_city(lat, long, model_type='predict')
    curr_time = datetime.datetime.now(tz=KST)
    delta = datetime.timedelta(hours=delay)

    if closest_city_id != None:
        closest_city = GlobalPredict.objects.get(
            city_id=closest_city_id)
        if curr_time - closest_city.updated_time < delta:
            # data is less than one hour old
            return closest_city
        else:
            # data is more than one hour old
            json_data = requests.get(predict_id.format(
                city_id=closest_city_id, api_key=WEATHER_API_KEY))
            json_dict = json.loads(json_data.text)
            cleaned_data = clean_names_predict(json_dict)
            # update date or make new data
            closest_city, bool_created = GlobalPredict.objects.update_or_create(
                city_id=cleaned_data['city_id'], defaults=cleaned_data)
            return closest_city
    else:  # if closest city ID is None:
        json_data = requests.get(predict_lat_long.format(
            lat=lat, long=long, api_key=WEATHER_API_KEY))
        json_dict = json.loads(json_data.text)
        cleaned_data = clean_names_predict(json_dict)
        # update or create city weather data
        closest_city, bool_created = GlobalPredict.objects.update_or_create(
            city_id=cleaned_data['city_id'], defaults=cleaned_data)
        return closest_city


# function to scrape current weather data if 1 hours has passed since last update_time
def domestic_initial_scrape(delay=1):
    # 한국 표준시간
    KST = datetime.timezone(datetime.timedelta(hours=9))
    # check whether scrapped in the last 12 hours
    curr_time = datetime.datetime.now(tz=KST)
    delta = datetime.timedelta(hours=delay)
    try:
        sample_city = DomesticCurrent.objects.get(id=1)
        # just return without updating if less than 1 hour has passed since last update
        if curr_time - sample_city.update_time < delta:
            return
    except:
        print("probably haven't done inital scrape yet")
        pass
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
        curr_city, bool_created = DomesticCurrent.objects.get_or_create(
            id=city_idx+1, location=city_data[0].text)
        cleaned_data = [city_data[idx].text if city_data[idx].text !=
                        '\xa0' else None for idx in valid_columns]
        curr_city.status, curr_city.temp, curr_city.windchill, curr_city.rain, curr_city.snow, curr_city.humidity, curr_city.wind_direction = cleaned_data
        curr_city.save()
