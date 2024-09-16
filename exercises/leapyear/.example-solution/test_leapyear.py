#!/usr/bin/env python3

import unittest
from leapyear import is_leap_year


class TestLeapYear(unittest.TestCase):
    def test_divisible_by_4_not_century(self):
        # Test if a year divisible by 4 but not a century is a leap year
        self.assertEqual(is_leap_year(2024), True)

    def test_not_divisible_by_4(self):
        # Test if a year not divisible by 4 is not a leap year
        self.assertEqual(is_leap_year(2019), False)

    def test_century_not_divisible_by_400(self):
        # Test if a century year not divisible by 400 is not a leap year
        self.assertEqual(is_leap_year(1900), False)

    def test_century_divisible_by_400(self):
        # Test if a century year divisible by 400 is a leap year
        self.assertEqual(is_leap_year(2000), True)

    def test_year_zero(self):
        # Test if the year 0 is a leap year
        self.assertEqual(is_leap_year(0), True)

    def test_negative_year(self):
        # Test if a negative year raises a ValueError
        with self.assertRaises(ValueError):
            is_leap_year(-2000)


if __name__ == "__main__":
    unittest.main()
