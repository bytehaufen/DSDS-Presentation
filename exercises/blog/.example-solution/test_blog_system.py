#!/usr/bin/env python3

import requests
import unittest


class TestBlogAPI(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    def test_get_posts(self):
        # Test call to get all
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_post(self):
        # Test create post
        new_post = {
            "title": "A day in the BA",
            "body": "That is not worth mentioning.",
            "userId": "Louis",
        }
        response = requests.post(self.BASE_URL, json=new_post)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], "A day in the BA")

    def test_update_post(self):
        # Test update a post
        updated_post = {
            "id": 1,
            "title": "Update on a day in the BA",
            "body": "It is much worse than expected.",
            "userId": "Louis",
        }
        response = requests.put(f"{self.BASE_URL}/1", json=updated_post)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Update on a day in the BA")

    def test_delete_post(self):
        # Test delete a post
        response = requests.delete(f"{self.BASE_URL}/1")
        self.assertEqual(response.status_code, 200)

    def test_get_nonexistent_post(self):
        # Test get a nonexistent post
        response = requests.get(f"{self.BASE_URL}/12309810923801")  # Nonexistent post
        self.assertEqual(response.status_code, 404)

    # NOTE: False responses - Failed tests

    def test_create_post_invalid_data(self):
        # Test create post with invalid data
        invalid_post = {
            "title": "",  # Empty title should be invalid
            "body": "I think i have to leave. It's so frustrating here.",
            "userId": "Louis",
        }
        response = requests.post(self.BASE_URL, json=invalid_post)
        # Any 4xx status code is expected, but a 201 is the response
        self.assertEqual(response.status_code, 404)

    def test_update_nonexistent_post(self):
        # Test delete a post
        updated_post = {
            "id": 9081327509387593845789357349,
            "title": "No body will find me",
            "body": "I've left. I'm now at a better place. Goodbye.",
            "userId": "Louis",
        }

        response = requests.put(
            f"{self.BASE_URL}/9081327509387593845789357349", json=updated_post
        )
        # Any 4xx status code is expected, but a 500 is thrown, because the API is not handling the error
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
