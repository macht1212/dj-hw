from rest_framework import serializers

from .models import MeasurementModel, SensorModel

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementModel
        fields = ['sensor', 'temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = SensorModel
        fields = ['id', 'name', 'description', 'measurements']


