import unittest
from run import Request

class RequestTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.request = Request('method', ['args'], {'opts': True})

    def test_method(self):
        self.assertEqual(self.request.method, 'method')
        
    def test_arguments(self):
        self.assertEqual(self.request.arguments, ['args'])
    
    def test_options(self):
        self.assertEqual(self.request.options, {'opts': True})

    def test_content(self):
        self.assertEqual(self.request.content, {
            'method': 'method',
            'arguments': ['args'],
            'options': {'opts': True},
        })                