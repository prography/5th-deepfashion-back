from django.db import models


# daily weather prediction from https://openweathermap.org/forecast5
# stores eight predictions of three hour intervals
class GlobalPredict(models.Model):
    # data that doesn't change
    city_country = models.TextField()
    city_name = models.TextField()
    city_id = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    #when the data was last updated
    update_time = models.TimeField(auto_now=True)

    # predictions that change
    # weather
    weather_id_one = models.IntegerField()
    weather_main_one = models.TextField()
    weather_description_one = models.TextField()
    weather_icon_one = models.TextField()
    # main
    temperatur_one = models.TextField()
    feels_like_one = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure_one = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity_one = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # wind
    wind_speed_one = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction_one = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # clouds
    cloud_one = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    predict_time_one = models.DateTimeField()

    # weather
    weather_id_two = models.IntegerField()
    weather_main_two = models.TextField()
    weather_description_two = models.TextField()
    weather_icon_two = models.TextField()
    # main
    temperatur_two = models.TextField()
    feels_like_two = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure_two = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity_two = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # wind
    wind_speed_two = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction_two = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # clouds
    cloud_two = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    predict_time_two = models.DateTimeField()


    # weather
    weather_id_three = models.IntegerField()
    weather_main_three = models.TextField()
    weather_description_three = models.TextField()
    weather_icon_three = models.TextField()
    # main
    temperatur_three = models.TextField()
    feels_like_three = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure_three = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity_three = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # wind
    wind_speed_three = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction_three = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # clouds
    cloud_three = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    predict_time_three = models.DateTimeField()


    # weather
    weather_id_four = models.IntegerField()
    weather_main_four = models.TextField()
    weather_description_four = models.TextField()
    weather_icon_four = models.TextField()
    # main
    temperatur_four = models.TextField()
    feels_like_four = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure_four = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity_four = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # wind
    wind_speed_four = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction_four = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # clouds
    cloud_four = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    predict_time_four = models.DateTimeField()


    # weather
    weather_id_five = models.IntegerField()
    weather_main_five = models.TextField()
    weather_description_five = models.TextField()
    weather_icon_five = models.TextField()
    # main
    temperatur_five = models.TextField()
    feels_like_five = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure_five = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity_five = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # wind
    wind_speed_five = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction_five = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # clouds
    cloud_five = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    predict_time_five = models.DateTimeField()




    # weather
    weather_id_six = models.IntegerField()
    weather_main_six = models.TextField()
    weather_description_six = models.TextField()
    weather_icon_six = models.TextField()
    # main
    temperatur_six = models.TextField()
    feels_like_six = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure_six = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity_six = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # wind
    wind_speed_six = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction_six = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # clouds
    cloud_six = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    predict_time_six = models.DateTimeField()




    # weather
    weather_id_seven = models.IntegerField()
    weather_main_seven = models.TextField()
    weather_description_seven = models.TextField()
    weather_icon_seven = models.TextField()
    # main
    temperatur_seven = models.TextField()
    feels_like_seven = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure_seven = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity_seven = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # wind
    wind_speed_seven = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction_seven = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # clouds
    cloud_seven = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    predict_time_seven = models.DateTimeField()



    # weather
    weather_id_eight = models.IntegerField()
    weather_main_eight = models.TextField()
    weather_description_eight = models.TextField()
    weather_icon_eight = models.TextField()
    # main
    temperatur_eight = models.TextField()
    feels_like_eight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure_eight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity_eight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # wind
    wind_speed_eight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction_eight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # clouds
    cloud_eight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    predict_time_eight = models.DateTimeField()





# current weather from https://openweathermap.org/current
class GlobalCurrent(models.Model):
    # coord
    longitude = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    latitude = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # weather
    weather_id = models.IntegerField()
    weather_main = models.TextField()
    weather_description = models.TextField()
    weather_icon = models.TextField()
    # main
    # clouds = models.TextField()
    temperature = models.TextField()
    feels_like = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # wind
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_direction = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # clouds
    cloud = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # rain
    rain_one_hour = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    rain_three_hour = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # snow
    snow_one_hour = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    snow_three_hour = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # dt, when the data was last calculated by the external weather api, unix time
    calculation_datatime = models.DateField()
    #sys
    city_country = models.TextField()
    # remaining
    city_id = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    city_name = models.TextField()

    #when the data was last updated
    update_time = models.TimeField(auto_now=True)






# current temp, wind direction, etc
# # http://www.weather.go.kr/weather/observation/currentweather.jsp
class DomesticCurrent(models.Model):
    # 지점 , 강릉 부터 흑산도 까지 
    location = models.TextField()
    # when the data was last updated
    update_time = models.DateTimeField(auto_now=True)
    # 현재일기
    status = models.TextField(null=True)
    # 현재기온
    temp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # 체감기온
    windchill_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # 강수량 mm
    rain = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # 적설량 cm
    snow = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # humidity
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # 풍향
    wind_direction = models.TextField(null=True)
    # 풍속
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)


    
# short term prediction from 기상청 날씨 누리
# http: // www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp
# 4 hour time period, 0th day to 2nd day predictions
# class ShortPredictionWeather(models.Model):
#     # when the data was last updated
#     update_time = models.DateTimeField(auto_now=True)
#     # 읍면동 코드
#     dong_code = models.BigIntegerField(null=True)
#     # 동네 이름 ex: 서울특별시 동작구 신대방제2동
#     location = models.TextField(null=True)
#     # published time, 기상청에서 발표한 시간
#     publish_time = models.TextField(null=True)
#     # next + seq number + data type

#     # data sequence 0
#     next_zero_hour = models.IntegerField(null=True)
#     next_zero_temp = models.DecimalField(
#         max_digits=5, decimal_places=2, null=True)
#     # weather status, 하늘 상태 코드, 맑음, 흐림. etc
#     next_zero_sky = models.IntegerField(null=True)
#     # 강수 상태 코드
#     next_zero_rain = models.IntegerField(null=True)
#     # 강수 확률
#     next_zero_rain_prob = models.DecimalField(max_digits=5, decimal_places=2, null=True)
#     next_zero_wind_speed = models.DecimalField(
#         max_digits=5, decimal_places=2, null=True)
#     next_zero_wind_direction = models.IntegerField(null=True)
#     next_zero_humidity = models.DecimalField(
#         max_digits=5, decimal_places=2, null=True)

#     # data sequence 1
#     next_one_hour = models.IntegerField(null=True)
#     next_one_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
#     next_one_sky = models.IntegerField(null=True)
#     next_one_rain = models.IntegerField(null=True)
#     next_one_rain_prob = models.DecimalField(max_digits=5, decimal_places=2, null=True)
#     next_one_wind_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
#     next_one_wind_direction = models.IntegerField(null=True)
#     next_one_humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)



