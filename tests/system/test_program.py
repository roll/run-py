import os
import unittest
from run import Program

class ProgramTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        os.chdir(self._get_fixtures_path())
    
    def test_build(self):
        program = Program(['run'])
        program()
        
    #Protected
    
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)