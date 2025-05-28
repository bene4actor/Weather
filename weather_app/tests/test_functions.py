import pytest
from weather_app.functions import unique_ordered, contains_cyrillic

def test_unique_ordered_basic():
    data = ["Apple", "banana", "apple", "Banana", "Cherry"]
    expected = ["Apple", "banana", "Cherry"]
    assert unique_ordered(data) == expected

def test_unique_ordered_empty():
    assert unique_ordered([]) == []

def test_unique_ordered_case_insensitive():
    data = ["a", "A", "b", "B", "a"]
    expected = ["a", "b"]
    assert unique_ordered(data) == expected

def test_contains_cyrillic_with_cyrillic():
    assert contains_cyrillic("Привет") is True
    assert contains_cyrillic("Hello мир") is True

def test_contains_cyrillic_without_cyrillic():
    assert contains_cyrillic("Hello world") is False
    assert contains_cyrillic("") is False
