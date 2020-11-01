import unittest
from application import routes

class TestRoutes(unittest.TestCase):
    def test_videos_data(self):
        routes.videos_data()


if __name__ == '__main__':
    unittest.main()
