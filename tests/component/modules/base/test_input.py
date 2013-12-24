import unittest
from run.modules.base import InputVar

class InputVarTest(unittest.TestCase):
    
    #Public
    
    def test(self):
        var = InputVar('text', module=None)
        self.assertEqual(var._prompt, 'text')
        self.assertEqual(var._error, 'Try again..')    