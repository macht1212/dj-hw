# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics
from .models import MeasurementModel, SensorModel
from .serializers import SensorDetailSerializer, MeasurementSerializer



class CreateSensorView(generics.ListCreateAPIView):
    queryset = SensorModel.objects.all()
    serializer_class = SensorDetailSerializer


class UpdateSensorView(generics.RetrieveUpdateAPIView):
    queryset = SensorModel.objects.all()
    serializer_class = SensorDetailSerializer


class CreateMeasurementView(generics.ListCreateAPIView):
    queryset = MeasurementModel.objects.all()
    serializer_class = MeasurementSerializer
    

class ListSensorDetailView(generics.ListAPIView):
    queryset = SensorModel.objects.all()
    serializer_class = SensorDetailSerializer

