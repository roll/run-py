import json
import unittest
import ipclight
from run import Packer, Request

class PackerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.packer = Packer()
        self.message = Request('method', ['args'], {'opts': True})
        
    def test_pack(self):
        transport_message = self.packer.pack(self.message, 'run-json-1.0')
        self.assertIsInstance(transport_message, ipclight.Request)
        self.assertEqual(transport_message.protocol, 'run-json-1.0')
        self.assertEqual(json.loads(transport_message.content), {
            'method': 'method',
            'arguments': ['args'],
            'options': {'opts': True},
        })  