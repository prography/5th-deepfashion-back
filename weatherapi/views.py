from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import *
from django.http import HttpResponse
from .get_api import *


@csrf_exempt
@api_view(['POST'])
def get_current_weather(request):
    weather_data = get_create_current_weather(
        request.data['latitude'], request.data['longitude'])
    serializer = InternationalCurrentSerializer(weather_data)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def get_predict_weather(request):
    weather_data = get_create_predict_weather(
        request.data['latitude'], request.data['longitude'])
    serializer = GlobalPredictSerializer(weather_data)
    return Response(serializer.data)


class DomesticCurrentView(generics.ListAPIView):
    queryset = DomesticCurrent.objects.all()
    serializer_class = DomesticCurrentSerializer

    def list(self, request):
        domestic_initial_scrape()
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = DomesticCurrentSerializer(queryset, many=True)
        return Response(serializer.data)
