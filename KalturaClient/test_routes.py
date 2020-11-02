import unittest
import requests
from kaltura_api_sessions.kaltura_envoke_sessions import add_media, delete, get_entry
import time
from application import app
from application import routes

base_url = 'http://127.0.0.1:5000/'
# base_url = 'https://kaltura-dan.herokuapp.com/'


class TestApi(unittest.TestCase):

    def test_get(self):
        with self.subTest('test that the Get api returns status code 200'):
            response = requests.get(url=base_url + '/api')
            self.assertEqual(response.status_code, 200)
        with self.subTest('test that the Get api returns status code 200'):
            self.assertEqual(type(response),  requests.models.Response)


    def test_delete(self):
        with self.subTest('deleting message runs successfully'):
            #creating video to delete
            add_media()
            time.sleep(60)



            idx = '1_kjqjmwyb'

            # verifying the video has uploaded to media
            response = requests.get(url=base_url + 'api/' + idx)
            self.assertIsInstance(response.json(), dict)
            self.assertEqual(response.status_code, 200)

            # Deleting video
            response = requests.delete(url=base_url + 'api/' + idx)
            self.assertEqual(response.json(), {'message': 'Entry item deleted!'})

            # verifying video is no longer in media
            response = requests.get(url=base_url + 'api/' + idx)
            self.assertIsInstance(response.json(), dict)
            self.assertEqual(response.status_code, 200)

        with self.subTest('deleting message fails due to non existing Id'):
            idx = 'fsdf'
            response = requests.delete(url=base_url + 'api/' + idx)
            self.assertEqual(response.json(), {'message': 'Entry deleted Failed!'})




if __name__ == '__main__':
    unittest.main()
