import os
import unittest
from run import Program

class ProgramTest(unittest.TestCase):

    #Public
    
    def test(self):
        os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
        program = Program(['run', 'render', '-d'])
        program()