import unittest
import ipclight
from run import Packer, Request

class PackerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.packer = Packer()
        self.protocol = 'run-json-1.0'
        self.method = 'method'
        self.arguments = ['arguments']
        self.options = {'options': True}
        self.message = Request(self.method, self.arguments, self.options)
        
    def test_pack(self):
        transport_message = self.packer.pack(self.message, self.protocol)
        self.assertIsInstance(transport_message, ipclight.Request)
        self.assertEqual(transport_message.protocol, self.protocol)
        #TODO: improve
        self.assertTrue(transport_message.content)