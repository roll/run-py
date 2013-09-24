import unittest
from run import Request

class RequestTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.request = Request('method', ['arg1'], {'kwarg1': True})

    def test_method(self):
        self.assertEqual(self.request.method, 'method')
        
    def test_args(self):
        self.assertEqual(self.request.args, ['arg1'])
    
    def test_kwargs(self):
        self.assertEqual(self.request.kwargs, {'kwarg1': True})

    def test_content(self):
        self.assertEqual(self.request.content, {
            'method': 'method',
            'args': ['arg1'],
            'kwargs': {'kwarg1': True},
        })                