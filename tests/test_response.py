import unittest
from run import Response

class ResponseTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.response = Response('result', 'error')

    def test_result(self):
        self.assertEqual(self.response.result, 'result')
        
    def test_error(self):
        self.assertEqual(self.response.error, 'error')

    def test_content(self):
        self.assertEqual(self.response.content, {
            'result': 'result',
            'error': 'error',
        })               