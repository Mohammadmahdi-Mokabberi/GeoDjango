from unicodedata import name
from requests import PreparedRequest
from rest_framework import serializers
from .models import Incidences

class LocationsSeraizlier(serializers.ModelSerializer):

    class Meta:
        model = Incidences
        fields = ['id', 'name']


class LocationDetailSerializer(serializers.ModelSerializer):
    location_x = serializers.CharField(source='get_location_x')
    location_y = serializers.CharField(source='get_location_y')

    class Meta:
        model = Incidences
        fields = ['id', 'name', 'image', 'location_x', 'location_y']


class CreateLocationSerializer(serializers.Serializer):
    name = serializers.CharField()
    location_x = serializers.CharField()
    location_y = serializers.CharField()
