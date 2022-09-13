import unittest
import app as tested_app
import json


class FlaskAppTests(unittest.TestCase):
    def test_get_welcome_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Welcome Weclouddata! v0.1')