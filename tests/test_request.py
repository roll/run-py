import unittest
from run import Request

class RequestTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.request = Request('method', ['arguments'], {'options': True})

    def test_method(self):
        self.assertEqual(self.request.method, 'method')
        
    def test_arguments(self):
        self.assertEqual(self.request.arguments, ['arguments'])
    
    def test_options(self):
        self.assertEqual(self.request.options, {'options': True})

    def test_content(self):
        self.assertEqual(self.request.content, {
            'method': 'method',
            'arguments': ['arguments'],
            'options': {'options': True},
        })                