from rest_framework import serializers
from .models import ParkingFacility


class ParkingFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingFacility
        fields = '__all__'