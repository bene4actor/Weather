from django.urls import path
from .views import weather_view, CityStatsAPIView

urlpatterns = [
    path("", weather_view, name="weather"),
    path('api/city-stats/', CityStatsAPIView.as_view(), name='city-stats'),
]
