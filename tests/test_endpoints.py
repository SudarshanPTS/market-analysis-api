import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_company_info_no_ticker(self):
        response = self.app.get('/company-info/')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Missing 'ticker' query parameter", response.data)

    def test_company_info_valid_ticker(self):
        response = self.app.get('/company-info/?ticker=AAPL')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Apple", response.data)

    def test_company_info_invalid_ticker(self):
        response = self.app.get('/company-info/?ticker=NOEXIST')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
