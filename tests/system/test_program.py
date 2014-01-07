import os
import unittest
from run import Program

#TODO: rewrite!
class ProgramTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    def test_render(self):
        program = Program(['run', 'render', '-d'])
        program()
        
    def test_meta(self):
        program = Program(['run', '-m'])
        program()