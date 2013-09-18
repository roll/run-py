import unittest
from run import Request

class RequestTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.message = Request()