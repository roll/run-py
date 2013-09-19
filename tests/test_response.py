import unittest
from run import Response

class ResponseTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.result = 'result'
        self.error = 'error'
        self.protocol = 'run-json-1.0'        
        self.response = Response(self.result, self.error)

    def test_result(self):
        self.assertEqual(self.response.result, self.result)
        
    def test_error(self):
        self.assertEqual(self.response.error, self.error)

    def test_protocol(self):
        self.assertEqual(self.response.protocol, self.protocol)

    def test_content(self):
        self.assertEqual(self.response.content, {
            'result': self.result,
            'error': self.error,
        })               