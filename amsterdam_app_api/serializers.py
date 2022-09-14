from rest_framework import serializers
from amsterdam_app_api.models import CityOffices
from amsterdam_app_api.models import CityOfficesOpeningHoursRegular
from amsterdam_app_api.models import CityOfficesOpeningHoursExceptions


class CityOfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityOffices
        fields = '__all__'


class CityOfficesOpeningHoursRegularSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityOfficesOpeningHoursRegular
        fields = '__all__'


class CityOfficesOpeningHoursExceptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityOfficesOpeningHoursExceptions
        fields = '__all__'
