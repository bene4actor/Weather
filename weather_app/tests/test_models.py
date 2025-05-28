import pytest
from django.utils import timezone
from weather_app.models import SearchHistory


@pytest.mark.django_db
def test_searchhistory_creation_and_str():
    city = "Москва"
    session_key = "test_session_key_12345"

    sh = SearchHistory.objects.create(city=city, session_key=session_key)

    assert sh.city == city
    assert sh.session_key == session_key
    # Проверяем, что searched_at установлен и близок к текущему времени
    assert (timezone.now() - sh.searched_at).total_seconds() < 10

    # Проверяем __str__
    expected_str_start = f"{city} @"
    assert sh.__str__().startswith(expected_str_start)
