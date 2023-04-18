""" Model Serializers """
from rest_framework import serializers
from amsterdam_app_api.models import CityOffices
from amsterdam_app_api.models import CityOfficesOpeningHoursRegular
from amsterdam_app_api.models import CityOfficesOpeningHoursExceptions


class CityOfficesSerializer(serializers.ModelSerializer):
    """ City Offices Serializer """
    class Meta:
        model = CityOffices
        fields = '__all__'


class CityOfficesOpeningHoursRegularSerializer(serializers.ModelSerializer):
    """ City Offices Opening Hours Regular Serializer"""
    class Meta:
        model = CityOfficesOpeningHoursRegular
        fields = '__all__'


class CityOfficesOpeningHoursExceptionsSerializer(serializers.ModelSerializer):
    """ City Offices Opening Hours Exceptions Serializer """
    class Meta:
        model = CityOfficesOpeningHoursExceptions
        fields = '__all__'
