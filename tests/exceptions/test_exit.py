import unittest
from run.exceptions.exit import HelpExit, ErrorExit

class HelpExitTest(unittest.TestCase):

    def setUp(self):
        self.exception = HelpExit()

    def test_status(self):
        self.assertEqual(self.exception.status, 0)
    
    def test_message(self):
        self.assertEqual(self.exception.message, '')
                
    def test_usage(self):
        self.assertEqual(self.exception.usage, False)

    def test_help(self):
        self.assertEqual(self.exception.help, True)

    def test_str(self):
        self.assertEqual(str(self.exception), '')
    

class ErrorExitTest(unittest.TestCase):

    def setUp(self):
        self.exception = ErrorExit(message='test', usage=True)

    def test_status(self):
        self.assertEqual(self.exception.status, 1)    
    
    def test_message(self):
        self.assertEqual(self.exception.message, 'test')
        
    def test_usage(self):
        self.assertEqual(self.exception.usage, True)

    def test_help(self):
        self.assertEqual(self.exception.help, False)
                
    def test_str(self):
        self.assertEqual(str(self.exception), 'test')                      