import unittest
from run import Response

class ResponseTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.result = 'result'
        self.error = 'error'
        self.response = Response(self.result, self.error)

    def test_result(self):
        self.assertEqual(self.response.result, self.result)
        
    def test_error(self):
        self.assertEqual(self.response.error, self.error)