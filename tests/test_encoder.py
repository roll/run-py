import unittest
from run import Encoder, Request

class EncoderTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.encoder = Encoder()
        
    def test_encode(self):
        message = Request('method')
        self.assertAlmostEqual(self.encoder.encode(message),
                               'request/run-json-1.0/{"method": "method"}')