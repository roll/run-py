import unittest
from ipclight import CommonMessage

class RequestTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.message = CommonMessage('protocol', 'content')

    def test_protocol(self):
        self.assertEqual(self.message.protocol, 'protocol')
    
    def test_content(self):
        self.assertEqual(self.message.content, 'content')                