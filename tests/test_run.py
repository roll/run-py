import unittest
from run import Run

#Tests

class ResponseTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.run = Run()
        
    def test_help(self):
        self.assertEqual(self.run.help(), 'echo\nhelp')
        
    def test_help_method(self):
        self.assertEqual(self.run.help('echo'), 'echo(content)\nReturns content')
        
        
#Fixtures

class Run(Run):
    
    #Public
    
    def echo(self, content):
        """
        Returns content
        """
        return content