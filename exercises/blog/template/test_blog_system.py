#!/usr/bin/env python3

import requests
import unittest


class TestBlogAPI(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    def test_get_posts(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

        # Uncomment the line below to see the content
        # print(response.json())


if __name__ == "__main__":
    unittest.main()
