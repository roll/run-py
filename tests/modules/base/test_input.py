import unittest
from run.modules.base import InputVar

class InputVarTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.var = InputVar('What is it?', module=None)          