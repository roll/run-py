import json
import unittest
from run import Unpacker, Request

class UnpackerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.unpacker = Unpacker()
        
    def test_unpack_request(self):
        message = self.unpacker.unpack('request/run-json-1.0/'+json.dumps({
            'method': 'method',
            'arguments': ['arguments'],
            'options': {'options': True},
        }))
        self.assertIsInstance(message, Request)
        self.assertEqual(message.protocol, 'run-json-1.0')
        self.assertEqual(message.method, 'method')
        self.assertEqual(message.arguments, ['arguments'])
        self.assertEqual(message.options, {'options': True})