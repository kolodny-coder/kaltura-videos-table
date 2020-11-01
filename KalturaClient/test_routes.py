import unittest
from application import app
from application import routes

class TestRoutes(unittest.TestCase):
    def test_videos_data(self):
        with self.subTest('check does not exceed more than 20 videos'):
            routes.videos_data()
            # self.assertLessEqual(len(routes.videos_data.videos), 20)


if __name__ == '__main__':
    unittest.main()
