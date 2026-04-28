import pytest
from main import count_vowels

def test_count_vowels_english():
    assert count_vowels("Apple") == 2

def test_count_vowels_ukrainian():
    assert count_vowels("Слава") == 2

def test_empty_string():
    with pytest.raises(ValueError, match="Текст порожній"):
        count_vowels("")