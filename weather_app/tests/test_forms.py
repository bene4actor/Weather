import pytest
from weather_app.forms import CityForm


def test_cityform_valid_data():
    form = CityForm(data={'city': 'Москва'})
    assert form.is_valid()
    assert form.cleaned_data['city'] == 'Москва'


def test_cityform_invalid_data():
    form = CityForm(data={'city': ''})  # пустое поле
    assert not form.is_valid()
    assert 'city' in form.errors


def test_cityform_widget_attrs():
    form = CityForm()
    city_field = form.fields['city']
    attrs = city_field.widget.attrs

    assert attrs.get('placeholder') == 'Введите название города'
    assert attrs.get('autofocus') == 'autofocus'
    assert 'form-control' in attrs.get('class', '')
    assert attrs.get('autocomplete') == 'off'
