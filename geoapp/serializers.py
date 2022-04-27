from unicodedata import name
from requests import PreparedRequest
from rest_framework import serializers
from .models import Incidences

class LocationsSeraizlier(serializers.ModelSerializer):

    class Meta:
        model = Incidences
        fields = ['id', 'name']


class LocationDetailSerializer(serializers.ModelSerializer):
    x = serializers.CharField(source='get_x')
    y = serializers.CharField(source='get_y')

    class Meta:
        model = Incidences
        fields = ['id', 'name', 'image', 'x', 'y']


class CreateLocationSerializer(serializers.Serializer):
    name = serializers.CharField()
    x = serializers.CharField()
    y = serializers.CharField()
