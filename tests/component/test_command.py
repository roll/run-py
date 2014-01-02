import unittest
from run.command import Command

class CommandTest(unittest.TestCase):
    
    #Public
    
    def test(self):
        command = Command(
            ['run', 'attribute', 'arg1,True,kwarg1=1,', 'kwarg2=1.5'])
        self.assertEqual(command.attribute, 'attribute')
        self.assertEqual(command.args, ['arg1', True])
        self.assertEqual(command.kwargs, {'kwarg1': 1, 'kwarg2': 1.5})
        
    def test_with_list_flag(self):
        command = Command(['run', 'attribute', '-l'])
        self.assertEqual(command.attribute, 'list')
        self.assertEqual(command.args, ['attribute'])
    
    def test_with_info_flag(self):
        command = Command(['run', 'attribute', '-i'])
        self.assertEqual(command.attribute, 'info')
        self.assertEqual(command.args, ['attribute'])    
        
    def test_with_meta_flag(self):
        command = Command(['run', 'attribute', '-m'])
        self.assertEqual(command.attribute, 'meta')
        self.assertEqual(command.args, ['attribute'])        
        
    def test_with_no_attribute(self):
        command = Command(['run'])
        self.assertEqual(command.attribute, command._default_attribute)