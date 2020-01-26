from django.db import models

# daily weather prediction from https://openweathermap.org/forecast5
# stores eight predictions of three hour intervals


class GlobalPredict(models.Model):
    data = models.TextField(default="empty")
    city_id = models.IntegerField()
    updated_time = models.DateTimeField(auto_now=True)
    longitude = models.DecimalField(
        max_digits=15, decimal_places=10, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)


class InternationalCurrent(models.Model):
    # coord
    longitude = models.DecimalField(
        max_digits=15, decimal_places=10, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    # weather
    weather_id = models.IntegerField()
    weather_main = models.TextField()
    weather_description = models.TextField()
    weather_icon = models.TextField()
    # main
    # clouds = models.TextField()
    temperature = models.TextField()
    feels_like = models.DecimalField(
        max_digits=10, decimal_places=3, null=True)
    pressure = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    humidity = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    # wind
    wind_speed = models.DecimalField(
        max_digits=10, decimal_places=3, null=True)
    wind_direction = models.DecimalField(
        max_digits=10, decimal_places=3, null=True)
    # clouds
    cloud = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    # rain
    rain_one_hour = models.DecimalField(
        max_digits=10, decimal_places=3, null=True)
    rain_three_hour = models.DecimalField(
        max_digits=10, decimal_places=3, null=True)
    # snow
    snow_one_hour = models.DecimalField(
        max_digits=10, decimal_places=3, null=True)
    snow_three_hour = models.DecimalField(
        max_digits=10, decimal_places=3, null=True)
    # dt, when the data was last calculated by the external weather api, unix time
    calculation_datatime = models.DateTimeField()
    #sys
    city_country = models.TextField()
    # remaining
    city_id = models.IntegerField()
    city_name = models.TextField()

    #when the data was last updated
    updated_time = models.DateTimeField(auto_now=True)


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
    temp = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # 체감기온
    windchill_temp = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    # 강수량 mm
    rain = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # 적설량 cm
    snow = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # humidity
    humidity = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # 풍향
    wind_direction = models.TextField(null=True)
    # 풍속
    wind_speed = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
