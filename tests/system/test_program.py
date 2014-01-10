import os
import unittest
from run import Program

#TODO: rewrite!
class ProgramTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    def test_build(self):
        program = Program(['run', 'build', '-d'])
        program()
        
    def test_meta(self):
        program = Program(['run', '-m'])
        program()