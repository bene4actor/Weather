from urllib.parse import urlencode

import requests
from asgiref.sync import sync_to_async
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CityForm
from .functions import unique_ordered, contains_cyrillic
from .models import SearchHistory
from googletrans import Translator

translator = Translator()


def get_weather_data(city):
    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 0,
        "longitude": 0,
        "current_weather": True
    }

    # Получение координат
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_response = requests.get(geo_url, params={"name": city})
    geo_data = geo_response.json()

    if "results" not in geo_data or len(geo_data["results"]) == 0:
        return None

    location = geo_data["results"][0]
    params["latitude"] = location["latitude"]
    params["longitude"] = location["longitude"]

    weather_response = requests.get(url, params=params)
    weather_data = weather_response.json()

    return {
        "city": city,
        "country": location["country"],
        "temperature": weather_data.get("current_weather", {}).get("temperature"),
        "windspeed": weather_data.get("current_weather", {}).get("windspeed"),
        "weathercode": weather_data.get("current_weather", {}).get("weathercode"),
    }


def weather_view(request):
    weather = None
    not_found = False
    if not request.session.session_key:
        request.session.create()  # чтобы session_key был

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_original = form.cleaned_data["city"]
            if contains_cyrillic(city_original):
                city_for_search = translator.translate(city_original, dest='en').text
            else:
                city_for_search = city_original

            request.session["last_city"] = city_original
            request.session["search_city"] = city_for_search
            SearchHistory.objects.create(
                city=city_original,
                session_key=request.session.session_key
            )

            base_url = reverse('weather')
            query_string = urlencode({'city': city_for_search})
            url = f"{base_url}?{query_string}"
            return redirect(url)
    else:
        form = CityForm(initial={"city": request.session.get("last_city", "")})
        city = request.GET.get("city")
        if city:
            weather = get_weather_data(city)
            if weather is None:
                not_found = True
        else:
            city = request.session.get("search_city")
            if city:
                weather = get_weather_data(city)
                if weather:
                    weather["city"] = request.session.get("last_city")

    recent_cities_qs = (
        SearchHistory.objects
        .filter(session_key=request.session.session_key)
        .order_by('-searched_at')
        .values_list('city', flat=True)
        .distinct()
    )
    recent_cities = unique_ordered(list(recent_cities_qs))[:5]

    return render(
        request,
        "weather/weather.html",
        {
            "form": form,
            "weather": weather,
            "recent_cities": recent_cities,
            "not_found": not_found
        }
    )


class CityStatsAPIView(APIView):
    def get(self, request):
        stats = (
            SearchHistory.objects
            .values('city')
            .annotate(count=Count('id'))
            .order_by('-count')
        )
        return Response({item['city']: item['count'] for item in stats})