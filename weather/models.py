from django.db import models


# current temp, wind direction, etc
# # http://www.weather.go.kr/weather/observation/currentweather.jsp
class CurrentWeather(models.Model):
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
class ShortPredictionWeather(models.Model):
    # when the data was last updated
    update_time = models.DateTimeField(auto_now=True)
    # 읍면동 코드
    dong_code = models.BigIntegerField(null=True)
    # 동네 이름 ex: 서울특별시 동작구 신대방제2동
    location = models.TextField(null=True)
    # published time, 기상청에서 발표한 시간
    publish_time = models.TextField(null=True)
    # next + seq number + data type

    # data sequence 0
    next_zero_hour = models.IntegerField(null=True)
    next_zero_temp = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    # weather status, 하늘 상태 코드, 맑음, 흐림. etc
    next_zero_sky = models.IntegerField(null=True)
    # 강수 상태 코드
    next_zero_rain = models.IntegerField(null=True)
    # 강수 확률
    next_zero_rain_prob = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    next_zero_wind_speed = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    next_zero_wind_direction = models.IntegerField(null=True)
    next_zero_humidity = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    # data sequence 1
    next_one_hour = models.IntegerField(null=True)
    next_one_temp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    next_one_sky = models.IntegerField(null=True)
    next_one_rain = models.IntegerField(null=True)
    next_one_rain_prob = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    next_one_wind_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    next_one_wind_direction = models.IntegerField(null=True)
    next_one_humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)



