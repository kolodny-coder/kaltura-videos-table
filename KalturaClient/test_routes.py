import time
import unittest
import requests
from kaltura_api_sessions.kaltura_envoke_sessions import add_media
from kaltura_api_sessions import list

# base_url = 'http://127.0.0.1:5000/'
base_url = 'https://kaltura-dan.herokuapp.com/'


class TestApi(unittest.TestCase):

    def test_get(self):
        with self.subTest('test that the Get api returns status code 200'):
            response = requests.get(url=base_url + '/api')
            self.assertEqual(response.status_code, 200)
        with self.subTest('test that the Get api returns response from the correct type'):
            self.assertEqual(type(response), requests.models.Response)

    def test_delete(self):
        with self.subTest('deleting message runs successfully'):
            # creating video to delete
            add_media()
            time.sleep(60)
            idx = list.result.objects[-1].id

            # verifying the video has uploaded to media
            response = requests.get(url=base_url + 'api/' + idx)
            self.assertIsInstance(response.json(), dict)
            self.assertEqual(response.status_code, 200)

            # Deleting video
            response = requests.delete(url=base_url + 'api/' + idx)
            self.assertEqual(response.json(), {'message': 'Entry item deleted!'})

            # verifying video is no longer in media
            response = requests.get(url=base_url + 'api/' + idx)
            self.assertEqual(response.json(), {'message': 'Failed to get entry!'})
            self.assertEqual(response.status_code, 200)

        with self.subTest('deleting message fails due to non existing Id'):
            idx = 'non_existing'
            response = requests.delete(url=base_url + 'api/' + idx)
            self.assertEqual(response.json(), {'message': 'Entry deleted Failed!'})


if __name__ == '__main__':
    unittest.main()
