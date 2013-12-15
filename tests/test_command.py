import unittest
from run import Command

class CommandTest(unittest.TestCase):
    
    #Public
    
    def test_argv1(self):
        command = Command(['run', '-f', 'file', 'attribute', 
                           'arg1,arg2,kwarg1=True,', 'kwarg2=2'])
        self.assertEqual(command.file, 'file')
        self.assertEqual(command.attribute, 'attribute')
        self.assertEqual(command.args, ['arg1', 'arg2'])
        self.assertEqual(command.kwargs, {'kwarg1': True, 'kwarg2': 2})
    
    def test_argv2(self):
        command = Command(['run', '-f', 'file', 'attribute', '3'])
        self.assertEqual(command.file, 'file')
        self.assertEqual(command.attribute, 'attribute')
        self.assertEqual(command.args, [3])
        self.assertEqual(command.kwargs, {})