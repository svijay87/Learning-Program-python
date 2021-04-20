import pytest

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 180

@pytest.mark.great
def test_greater_equal():
    num = 100
    assert  num >= 100

@pytest.mark.skip
@pytest.mark.other
def less_test():
    num = 100
    assert num < 130