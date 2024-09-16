#!/usr/bin/env python3

import unittest
from leapyear import is_leap_year


class TestLeapYear(unittest.TestCase):
    def test_dummy(self):
        self.assertTrue(is_leap_year(2024))


if __name__ == "__main__":
    unittest.main()
