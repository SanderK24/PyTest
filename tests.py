import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_multiply(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_division(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_multiply_calculate_subtraction(self):
        assert self.calc.subtraction(self, 15, 7) == 8

    def test_multiply_calculate_adding(self):
        assert self.calc.adding(self, 8, 2) == 10