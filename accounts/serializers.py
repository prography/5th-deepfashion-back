from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Style
User = get_user_model()


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['id', 'name']


class AccountSerializer(serializers.ModelSerializer):
    # styles = StyleSerializer(many=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'gender', 'styles', 'password']

    def create(self, validated_data):
        print(validated_data)
        styles =validated_data.pop('styles')
        # print(styles)
        instance = self.Meta.model.objects.create_user(**validated_data)
        instance.styles.add(*styles)
        return instance




