from django.urls import path

from .views import CreateSensorView, UpdateSensorView, CreateMeasurementView, ListSensorDetailView

urlpatterns = [
    path('add_sensor/', CreateSensorView.as_view()),
    path('update_sensor/<pk>/', UpdateSensorView.as_view()),
    path('add_measurement/', CreateMeasurementView.as_view()),
    path('list_sensors/<pk>/', ListSensorDetailView.as_view())
]
