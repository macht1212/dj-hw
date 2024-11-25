from django.db import models


class SensorModel(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


class MeasurementModel(models.Model):
    
    temperature = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor_name = models.ForeignKey(SensorModel, on_delete=models.CASCADE, related_name='sensor')
    
