import sys
import unittest
from lib31.patcher import Patcher
from run import Program
from run.scripts.run import run
from ..fixtures import CLICommand

#Environment
Program


#Tests
class RunTest(unittest.TestCase):

    PATCH = {
        'Program.process': lambda self: 'process',    
    } 
    
    def setUp(self):
        self.patcher = Patcher(globals())
        self.patcher.patch(self.PATCH)
        self.cli = CLICommand()
        sys.argv = self.cli.argv
          
    def tearDown(self):
        self.patcher.restore()
        
    def test_run(self):
        self.assertEqual(run(), 'process')