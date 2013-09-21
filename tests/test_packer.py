import json
import unittest
import ipclight
from run import Packer, Request

class PackerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.packer = Packer()
        
    def test_pack_request(self):
        message = Request('method', ['arguments'], {'options': True})
        transport_message = self.packer.pack(message, 'run-json-1.0')
        self.assertIsInstance(transport_message, ipclight.Request)
        self.assertEqual(transport_message.protocol, 'run-json-1.0')
        self.assertEqual(json.loads(transport_message.content), {
            'method': 'method',
            'arguments': ['arguments'],
            'options': {'options': True},
        })  