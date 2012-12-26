import unittest
from run import Command, Driver
from .fixtures import CLICommand
    
#Fixtures    
class BaseDriverImp(Driver):

    def process(self):
        return 'process'
    

#Tests
class BaseDriverTest(unittest.TestCase):

    def setUp(self):
        self.cli = CLICommand()
        self.command = Command(self.cli.argv)
        self.driver = BaseDriverImp(self.command)
     
    def test_process(self):
        self.assertEqual(self.driver.process(), 'process')