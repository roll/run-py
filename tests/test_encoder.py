import unittest
from run import Encoder, Response

class EncoderTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.encoder = Encoder()
        
    def test_encode(self):
        message = Response('result')