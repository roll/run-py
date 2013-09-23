import unittest
from run import Run

#Tests

class ResponseTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.run = EchoRun() 
        
        
#Fixtures

class EchoRun(Run):
    
    #Public
    
    def echo(self, content):
        """
        Returns content
        """
        return content