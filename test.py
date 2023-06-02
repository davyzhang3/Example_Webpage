import unittest
import app as tested_app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_welcome_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Welcome Weclouddata! v0.6')


    def test_get_courses_endpoint(self):
        r = self.app.get('/courses')
        self.assertEqual(r.data, b'DevOps')
if __name__ == '__main__':
    unittest.main()