from app.models import User
from app import db
import unittest

class UserTest(unittest.TestCase):
    '''Class to test user.
    '''
    def setUp(self):
        self.test_user = User(password='t3st')

    def test_password_setter(self):
        self.assertTrue(self.test_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.test_user.verify_password('test'))