import unittest
from run import Command
from run.drivers.base import BaseDriver
from ...fixtures import CLICommand
    
#Fixtures    
class BaseDriverImp(BaseDriver):

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