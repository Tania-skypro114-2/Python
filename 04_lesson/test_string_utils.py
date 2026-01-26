import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("привет", "Привет"),
    ("добрый день", "Добрый день")
   ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("1a5", "1a5"),
    ("", "")
    ])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" привет", "привет")
    ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" привет ", "привет ")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
    ("привет", "е", True),
    ("привет", "а", False)
])
def test_contains_positive(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, result", [
    ("привет", "П", False),
    ("привет", " ", False)
])
def test_contains_negative(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
    ("привет", "ив", "прет"),
    ("мой день", "мой", " день")
])
def test_delete_symbol_positive(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, result", [
    (" ", " ", ""),
    ("привет", "s", "привет")
])
def test_delete_symbol_negative(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result
