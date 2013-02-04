import unittest
from lib31.patcher import Patcher
from run.console.command import Command
from run.console.program import Program
from run.exceptions.exit import HelpExit, ErrorExit

#Environment
Command


#Fixtures
class Driver_normal(object):

    def process(self, *args, **kwargs):
        pass

    
class Driver_help_exit(object):
    
    def process(self, *args, **kwargs):
        raise HelpExit()

    
class Driver_error_exit(object):
    
    def process(self, *args, **kwargs):
        raise ErrorExit('message')    


#Tests
class ProgramTest(unittest.TestCase):

    def setUp(self):
        self.patcher = Patcher(globals())
        self.patcher.patch(self.PATCH)
        self.program = Program(['run', '-h'])
        
    def tearDown(self):
        self.patcher.restore()
        
        
class ProgramTest_normal(ProgramTest):                
    
    PATCH = {
        'Command.driver': Driver_normal(),
    }
    
    def test(self):
        self.program.process()
        
        
class ProgramTest_help_exit(ProgramTest):                
    
    PATCH = {
        'Command.driver': Driver_help_exit(),         
    }
        
    def test(self):
        self.assertRaises(SystemExit, self.program.process)
                
        
class ProgramTest_error_exit(ProgramTest):                
    
    PATCH = {
        'Command.driver': Driver_error_exit(),         
    }
        
    def test(self):
        self.assertRaises(SystemExit, self.program.process)        