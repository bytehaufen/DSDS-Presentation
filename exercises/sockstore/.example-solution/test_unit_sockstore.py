#!/usr/bin/env python3

# Example Unit tests for the `Sockenversand-stretched-out` Exercise

import unittest
from sockstore import SockStore


class TestSockStore(unittest.TestCase):
    def setUp(self):
        self.store = SockStore()

    def test_add_sock(self):
        # Test if a sock can be added to the store
        self.store.add_sock("red", 5)
        self.assertEqual(self.store.search("red"), 5)

    def test_add_negative_quantity(self):
        # Test if adding a negative quantity of socks raises a ValueError
        with self.assertRaises(ValueError):
            self.store.add_sock("red", -5)

    def test_search(self):
        # Test if the search function returns the correct quantity of a specific sock
        self.assertEqual(self.store.search("blue"), 0)
        self.store.add_sock("blue", 3)
        self.assertEqual(self.store.search("blue"), 3)

    def test_buy_sock(self):
        # Test if a sock can be bought from the store
        self.store.add_sock("green", 2)
        self.store.buy_sock("green")
        self.assertEqual(self.store.search("green"), 1)

    def test_add_buy_multiple_colors(self):
        # Test if multiple colors of socks can be added and bought from the store
        self.store.add_sock("red", 5)
        self.store.add_sock("blue", 3)
        self.assertEqual(self.store.search("red"), 5)
        self.assertEqual(self.store.search("blue"), 3)
        self.store.buy_sock("red")
        self.store.buy_sock("blue")
        self.assertEqual(self.store.search("red"), 4)
        self.assertEqual(self.store.search("blue"), 2)

    def test_buy_sock_never_added(self):
        # Test if buying a sock that was never added to the store raises a ValueError
        with self.assertRaises(ValueError):
            self.store.buy_sock("orange")

    def test_buy_sock_no_stock(self):
        # Test if buying a sock that is not in stock raises a ValueError
        with self.assertRaises(ValueError):
            self.store.buy_sock("purple")

    def test_buy_sock_out_of_stock(self):
        # Test if buying a sock that is out of stock raises a ValueError
        self.store.add_sock("yellow", 1)
        self.store.buy_sock("yellow")
        with self.assertRaises(ValueError):
            self.store.buy_sock("yellow")

    def test_buy_more_than_available(self):
        # Test if buying more socks than available raises a ValueError
        self.store.add_sock("green", 2)
        with self.assertRaises(ValueError):
            for _ in range(3):
                self.store.buy_sock("green")


if __name__ == "__main__":
    unittest.main()
