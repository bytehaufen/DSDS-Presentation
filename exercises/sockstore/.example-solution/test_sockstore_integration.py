#!/usr/bin/env python3

# Example Integration tests for the `Sockenversand-stretched-out` Exercise

import unittest
from sockstore import SockStore


class TestSockStoreIntegration(unittest.TestCase):
    def setUp(self):
        self.store = SockStore()

    def test_integration(self):
        # Test adding socks
        self.store.add_sock("red", 5)
        self.store.add_sock("blue", 3)
        self.store.add_sock("green", 2)

        # Test searching for socks
        self.assertEqual(self.store.search("red"), 5)
        self.assertEqual(self.store.search("blue"), 3)
        self.assertEqual(self.store.search("green"), 2)

        # Test buying socks
        self.store.buy_sock("red")
        self.store.buy_sock("blue")
        self.store.buy_sock("green")

        # Test searching for socks after buying
        self.assertEqual(self.store.search("red"), 4)
        self.assertEqual(self.store.search("blue"), 2)
        self.assertEqual(self.store.search("green"), 1)

        # Test buying more socks than available
        with self.assertRaises(ValueError):
            for _ in range(5):
                self.store.buy_sock("green")

        # Test searching for socks after trying to buy more than available
        self.assertEqual(self.store.search("green"), 1)

        # Test buying socks that were never added
        with self.assertRaises(ValueError):
            self.store.buy_sock("purple")

        # Test searching for socks that were never added
        self.assertEqual(self.store.search("purple"), 0)


if __name__ == "__main__":
    unittest.main()
