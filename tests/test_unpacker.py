import json
import unittest
import ipclight
from run import Unpacker, Request

class UnpackerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.unpacker = Unpacker()
        
    def test_unpack_request(self):
        transport_message = ipclight.Request('run-json-1.0',json.dumps({
            'method': 'method',
            'arguments': ['arguments'],
            'options': {'options': True},
        }))
        message = self.unpacker.unpack(transport_message)
        self.assertIsInstance(message, Request)
        self.assertEqual(message.method, 'method')
        self.assertEqual(message.arguments, ['arguments'])
        self.assertEqual(message.options, {'options': True})