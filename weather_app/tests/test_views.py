import pytest
import sys
from django.urls import reverse
from rest_framework.test import APIClient

from weather_app.models import SearchHistory


@pytest.mark.django_db
def test_weather_view_get(client):
    url = reverse('weather')
    response = client.get(url)
    assert response.status_code == 200
    assert "text/html" in response['Content-Type']
    assert 'form' in response.context

@pytest.mark.django_db
def test_weather_view_post_creates_search_history(client):
    url = reverse('weather')
    city_name = "Moscow"
    response = client.post(url, data={"city": city_name})
    assert response.status_code == 302
    assert SearchHistory.objects.filter(city=city_name).exists()

@pytest.mark.django_db
def test_city_stats_api(client):
    SearchHistory.objects.create(city="Москва", session_key="abc")
    SearchHistory.objects.create(city="Москва", session_key="def")
    SearchHistory.objects.create(city="Питер", session_key="abc")

    client = APIClient()
    url = reverse('city-stats')
    response = client.get(url)
    assert response.status_code == 200

    data = response.json()

    assert data.get("Москва") == 2
    assert data.get("Питер") == 1
