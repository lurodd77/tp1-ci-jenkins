from app import addition

def test_addition_positive():
    assert addition(2, 3) == 5

def test_addition_negative():
    assert addition(-1, -2) == -3

def test_addition_zero():
    assert addition(0, 5) == 5
    assert addition(0, 0) == 0

def test_addition_float():
    assert addition(1.5, 2.5) == 4.0
