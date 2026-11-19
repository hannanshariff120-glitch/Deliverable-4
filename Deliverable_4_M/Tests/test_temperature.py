import pytest
from Temperature import Temperature


def test_case_insensitive_unit():
    temp = Temperature(25, "c")
    assert temp.value == 25
    assert temp.unit == "C"


@pytest.mark.parametrize("unit, expected_unit", [("c", "C"),
                                                 ("k", "K"),
                                                 ("f", "F"),
                                                 ("C", "C"),
                                                 ("K", "K"),
                                                 ("F", "F")])
def test_case_all_units(unit, expected_unit):
    temp = Temperature(25, unit)
    assert temp.value == 25
    assert temp.unit == expected_unit


def test_invalid_unit_raises_exception():
    with pytest.raises(ValueError, match="The temperature must be in C, K or F"):
        Temperature(25, "p")


def test_read_only_behavior_for_value():
    with pytest.raises(AttributeError):
        temp = Temperature(25, "c")
        temp.value = 30

def test_read_only_behavior_for_unit():
    with pytest.raises(AttributeError):
        temp = Temperature(25, "c")
        temp.unit = "F"


@pytest.mark.parametrize("value, unit", [(-300, "C"),
                                         (-500, "F"),
                                         (-1, "K")])
def test_temperatures_below_absolute_zero(value, unit):
    with pytest.raises(ValueError):
        Temperature(value, unit)
