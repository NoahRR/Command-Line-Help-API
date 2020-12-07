from app import app
import unittest
import requests

API_URL = 'http://127.0.0.1:8001/'

class test_endpoints(unittest.TestCase):

    def test1_ping(self):
        response = requests.get(API_URL)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
