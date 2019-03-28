import os, sys
from flask_testing import TestCase

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import create_flask_app


class BaseTestCase(TestCase):

    def create_app(self):
        self.app = create_flask_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        return self.app


    def tearDown(self):
        self.app_context.pop()