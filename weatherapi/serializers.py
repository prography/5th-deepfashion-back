from .models import *
from rest_framework import serializers


class DomesticCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomesticCurrent
        fields = "__all__"


class InternationalCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalCurrent
        fields = "__all__"


class GlobalPredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalPredict
        fields = "__all__"
