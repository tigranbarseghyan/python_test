import main

def test_sum():
    assert main.msum(10, 20) == 30

def test_sub():
    assert main.msub(20, 10) == 10

def test_sum1():
    assert main.msum(10, 30) == 41