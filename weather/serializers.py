from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import *
from rest_framework import serializers

# 크롤링 libs
import requests
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import json


class CurrentWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentWeather
        fields = "__all__"



class ShortPredictionWeatherSerializer(serializers.ModelSerializer):
    pass
