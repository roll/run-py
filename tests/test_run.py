import unittest
from run import Run

#Tests

class ResponseTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.run = EchoRun()
        
    def test_help(self):
        self.assertEqual(self.run.help(), 'echo\nhelp') 
        
        
#Fixtures

class EchoRun(Run):
    
    #Public
    
    def echo(self, content):
        """
        Returns content
        """
        return content