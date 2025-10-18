import unittest
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app

class TestVotingSystem(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Online Voting System', response.data)

    def test_register_page(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Voter Registration', response.data)

    def test_admin_login_page(self):
        response = self.app.get('/admin_login_page')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Administrator Access', response.data)

if __name__ == '__main__':
    unittest.main()
