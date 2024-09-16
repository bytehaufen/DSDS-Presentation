#!/usr/bin/env python3


def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.

    A leap year is exactly divisible by 4 except for century years (years ending with 00).
    The century year is a leap year only if it is perfectly divisible by 400.

    Args:
        year (int): The year to check.

    Raises:
        ValueError: If the year is negative.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    divisible_by_4 = year % 4 == 0
    not_century = year % 100 != 0
    divisible_by_400 = year % 400 == 0

    if year < 0:
        raise ValueError("Year cannot be negative")

    return divisible_by_4 and (not_century or divisible_by_400)
