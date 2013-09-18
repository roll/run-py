import unittest
from run import Request

class RequestTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.arguments = ['arguments']
        self.options = {'options': True}
        self.request = Request(self.arguments, self.options)

    def test_arguments(self):
        self.assertEqual(self.request.arguments, self.arguments)
    
    def test_options(self):
        self.assertEqual(self.request.options, self.options)