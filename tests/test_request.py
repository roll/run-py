import unittest
from run import Request

class RequestTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.method = 'method'
        self.arguments = ['arguments']
        self.options = {'options': True}
        self.request = Request(self.method, self.arguments, self.options)

    def test_method(self):
        self.assertEqual(self.request.method, self.method)
        
    def test_arguments(self):
        self.assertEqual(self.request.arguments, self.arguments)
    
    def test_options(self):
        self.assertEqual(self.request.options, self.options)

    def test_content(self):
        self.assertEqual(self.request.content, {
            'method': self.method,
            'arguments': self.arguments,
            'options': self.options,
        })                