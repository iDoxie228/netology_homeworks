from django.urls import path
from .views import SensorsListCreate, SensorsRetrieveUpdate, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorsListCreate.as_view()),
    path('sensors/<int:pk>/', SensorsRetrieveUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view())
]
