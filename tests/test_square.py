import math
import pytest

@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num)  == 5

@pytest.mark.square
def test_square():
    num = 8
    assert  8*8 == 60

@pytest.mark.other
def tesequality():
    # function tesequality is not executed because pytest will not consider it as a test since its name is not of the format test*.
    assert 10 == 11