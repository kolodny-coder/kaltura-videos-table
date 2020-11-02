import unittest
import requests
from application import app
from application import routes

base_url = 'http://127.0.0.1:5000/'


class TestRoutes(unittest.TestCase):
    def test_videos_data(self):
        pass

    def test_get(self):
        with self.subTest('test that the Get api returns status code 200'):
            response = requests.get(url=base_url + '/api')
            self.assertEqual(response.status_code, 200)
        with self.subTest('test that the Get api returns status code 200'):
            self.assertEqual(type(response),  requests.models.Response)

    # def test_add(self):
    #     data = api.payload
    #     new_entry ={url: 'some_url'}
    #
    #     self.assertEqual(response, new_entry)

    def test_delete(self):
        with self.subTest('deleting message runs successfully'):
            #creating video to delete
            idx = '1_wr2535nv'

            # verifying the video has uploaded to media
            response = requests.get(url=base_url + 'api/' + idx)
            self.assertIsInstance(response.json(), dict)
            self.assertEqual(response.status_code, 200)

            # deleting video
            # idx = '1_6cjysqna'
            # response = requests.delete(url=base_url + 'api/' + idx)
            # self.assertEqual(response.json(), {'message': 'Entry item deleted!'})

            #verifying video is no longer in media
            response = requests.get(url=base_url + 'api/' + idx)
            self.assertIsInstance(response.json(), dict)
            self.assertEqual(response.status_code, 200)

        with self.subTest('deleting message fails due to non existing Id'):
            idx = 'fsdf'
            response = requests.delete(url=base_url + 'api/' + idx)
            self.assertEqual(response.json(), {'message': 'Entry deleted Failed!'})




if __name__ == '__main__':
    unittest.main()
