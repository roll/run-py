import unittest
from run import Decoder, Request

class DecoderTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.decoder = Decoder()
        
    def test_decode(self):
        text_message = 'request/run-json-1.0/{"method": "method"}'
        message = self.decoder.decode(text_message)
        self.assertIsInstance(message, Request)
        self.assertEqual(message.method, 'method')   