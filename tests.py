from app import app
import unittest
import requests


# base url
API_URL = 'http://127.0.0.1:8001/'

# contains urls to test along with their correct status codes
API_TESTING_URLS = [
    {'url': API_URL, 'status_code': 200},
    {'url': API_URL + 'all', 'status_code': 200},
    {'url': API_URL + 'search', 'status_code': 404},
    {'url': API_URL + 'search/file', 'status_code': 200},
    {'url': API_URL + 'search/copy', 'status_code': 200},
    {'url': API_URL + 'search/asgasdkg', 'status_code': 404}
]

# for dev testing
dev_url = API_URL + 'dev'
id1 = None
id2 = None


# testing status codes for all endpoints
class test_endpoints_non_dev(unittest.TestCase):

    def test_all(self):

        for item in API_TESTING_URLS:
            response = requests.get( item['url'] )
            self.assertEqual(response.status_code, item['status_code'])


# testing status codes and content for dev actions
# GET, POST, PUT, DELETE
class test_all_dev(unittest.TestCase):

    def test2_dev_GET(self):

        response = requests.get(dev_url)
        self.assertEqual(response.status_code, 200)

    # all 3 grouped here because:
    # they need to pass on ids
    def test3_POST_PUT_DEL(self):

        # POST without tags
        data = {
            'name': 'testHINT',
            'description': 'desc here'
        }

        response = requests.post(dev_url, params=data)

        resp_name = response.json()['Added new hint']['name']
        resp_desc = response.json()['Added new hint']['description']

        id1 = response.json()['Added new hint']['id']

        self.assertEqual(response.status_code, 201)
        self.assertEqual(resp_name, 'testHINT')
        self.assertEqual(resp_desc, 'desc here')


        # POST with tags
        data = {
            'name': 'testHINT2',
            'description': 'ooo a desc',
            'tags': 'one, two, tag'
        }

        response = requests.post(dev_url, params=data)

        resp_name = response.json()['Added new hint']['name']
        resp_desc = response.json()['Added new hint']['description']
        resp_tags = response.json()['Added the following tags']

        id2 = response.json()['Added new hint']['id']

        self.assertEqual(response.status_code, 201)
        self.assertEqual(resp_name, 'testHINT2')
        self.assertEqual(resp_desc, 'ooo a desc')
        self.assertEqual(resp_tags, ['one', 'two', 'tag'])


        # PUT
        data = {
            'id': id1,
            'name': 'newtestHINT',
            'description': 'new test dest',
            'tags': 'new1, new2'
        }

        response = requests.put(dev_url, params=data)

        resp_name = response.json()['Updated hint']['name']
        resp_desc = response.json()['Updated hint']['description']
        resp_tags = response.json()['Added the following tags']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resp_name, 'newtestHINT')
        self.assertEqual(resp_desc, 'new test dest')
        self.assertEqual(resp_tags, ['new1', 'new2'])


        # DELETE
        response1 = requests.delete(dev_url, params={'id': id1})
        response2 = requests.delete(dev_url, params={'id': id2})

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)


if __name__ == "__main__":
    unittest.main()
