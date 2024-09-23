#!/usr/bin/env python3

"""
Why is the original implementation bad?
Some reasons:
> - Deterministic and predictable: The seed is directly taken modulo 10,
>   which only generates 10 possible outputs, making it far from random.
> - Time dependency: The use of current time (time.time()) leads to output
>   that remains consistent over short periods. This makes the generator
>   both predictable and insecure.
"""

import unittest
from bestRndGenEver import bestRndGenEver


class TestBestRndGenEver(unittest.TestCase):
    # This only covers some of the tests that a true random number generator
    # should pass.

    def test_uniqueness_of_random_numbers(self):
        # Test if the random generator produces different values on multiple calls
        result1: str = bestRndGenEver()
        result2: str = bestRndGenEver()
        self.assertNotEqual(result1, result2)

    def test_uniqueness_of_random_numbers_in_bulk(self):
        # Test if the random generator produces a wide variety of values on many calls
        iterations = 1000
        results = [bestRndGenEver() for _ in range(iterations)]

        # Check that all values are unique
        unique_results = set(results)
        self.assertEqual(len(unique_results), iterations)

    def test_entropy_source(self):
        # Test if the random generator uses a sufficient number of bits (at least 64 bits)
        result = bestRndGenEver()
        random_number = int(result)
        # Verify that the generated random number uses at least 64 bits
        self.assertGreaterEqual(random_number.bit_length(), 64)

    def test_statistical_randomness(self):
        # Test if the random generator produces statistically random values
        iterations = 10000
        results = [int(bestRndGenEver()) for _ in range(iterations)]
        # Calculate the mean of the generated random numbers
        mean = sum(results) / iterations
        # Expected mean for a 64-bit random value
        expected_mean = (2**64 - 1) / 2
        # Check if the calculated mean is close to the expected mean
        self.assertAlmostEqual(mean, expected_mean, delta=expected_mean * 0.05)


if __name__ == "__main__":
    unittest.main()
