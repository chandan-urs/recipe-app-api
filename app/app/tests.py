from django.test import TestCase

from app.calc import add, sub


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(sub(5, 10), 5)
