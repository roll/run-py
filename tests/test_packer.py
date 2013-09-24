import json
import unittest
import ipclight
from run import Packer, Request, Response, PackError

class PackerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.packer = Packer()
        
    def test_pack_request(self):
        message = Request('method', ['arg1'], {'kwarg1': True})
        transport_message = self.packer.pack(message)
        self.assertIsInstance(transport_message, ipclight.Request)
        self.assertEqual(transport_message.protocol, 'run-json-1.0')
        self.assertEqual(json.loads(transport_message.content), {
            'method': 'method',
            'args': ['arg1'],
            'kwargs': {'kwarg1': True},
        })
        
    def test_pack_response(self):
        message = Response('result', 'error')
        transport_message = self.packer.pack(message, 'run-json-1.0')
        self.assertIsInstance(transport_message, ipclight.Response)
        self.assertEqual(transport_message.protocol, 'run-json-1.0')
        self.assertEqual(json.loads(transport_message.content), {
            'result': 'result',
            'error': 'error',
        })
        
    def test_pack_untyped_message(self):
        message = 'untyped_message'
        self.assertRaises(PackError, self.packer.pack, message, 'run-json-1.0')
    
    def test_pack_unsupported_protocol(self):
        message = Request('method')
        self.assertRaises(PackError, self.packer.pack, message, 'unsupported_protocol')                         