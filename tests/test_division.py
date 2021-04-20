import pytest

# @pytest.fixture
# def input_value():
#     val = 36
#     return val

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_12(input_value):
    assert input_value % 12 == 0

def test_divisible_by_10(input_value):
    assert input_value % 10  == 0