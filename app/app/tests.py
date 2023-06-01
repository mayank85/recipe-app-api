"""
Sample Tests
"""

from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """test adding two numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract(self):
        """Test the subtraction function"""
        res = calc.subtract(15, 10)

        self.assertEqual(res, -5)
