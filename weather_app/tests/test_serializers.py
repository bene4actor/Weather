import pytest
from weather_app.serializers import CityStatsSerializer

def test_serializer_valid_data():
    data = {'city_name': 'Москва', 'count': 5}
    serializer = CityStatsSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data['city_name'] == 'Москва'
    assert serializer.validated_data['count'] == 5

def test_serializer_invalid_data():
    # count должен быть целым числом, а тут строка
    data = {'city_name': 'Москва', 'count': 'five'}
    serializer = CityStatsSerializer(data=data)
    assert not serializer.is_valid()
    assert 'count' in serializer.errors

def test_serializer_missing_fields():
    data = {'city_name': 'Москва'}
    serializer = CityStatsSerializer(data=data)
    assert not serializer.is_valid()
    assert 'count' in serializer.errors
