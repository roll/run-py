import json
import unittest
import ipclight
from run import Unpacker, Request, Response, UnpackError

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
    
    def test_unpack_response(self):
        transport_message = ipclight.Response('run-json-1.0',json.dumps({
            'result': 'result',
            'error': 'error',
        }))
        message = self.unpacker.unpack(transport_message)
        self.assertIsInstance(message, Response)
        self.assertEqual(message.result, 'result')
        self.assertEqual(message.error, 'error')
        
    def test_unpack_untyped_message(self):
        transport_message = 'untyped_message'
        self.assertRaises(UnpackError, self.unpacker.unpack, transport_message)
        
    def test_unpack_usupported_protocol(self):
        transport_message = ipclight.Request('usupported_protocol', 'content')
        self.assertRaises(UnpackError, self.unpacker.unpack, transport_message)         