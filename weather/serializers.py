# from rest_framework.response import Response
# from rest_framework import authentication, permissions
from .models import *
from rest_framework import serializers

# import requests
# import urllib
# from bs4 import BeautifulSoup
# import pandas as pd
# import json


class DomesticCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomesticCurrent
        fields = "__all__"



class GlobalCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalCurrent
        fields = "__all__"


class GlobalPredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalPredict
        fields = "__all__"
