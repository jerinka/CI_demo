"""
Unit test for calculator"
"""


import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 2 == calculator.sub(4, 2)
    
    def test_mul(self):
        assert 100 == calculator.mul(10, 10)
