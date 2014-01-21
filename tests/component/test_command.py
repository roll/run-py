import unittest
from run.command import Command

class CommandTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.command = Command(['run'])
        
    def test_attribute(self):
        self.assertEqual(self.command.attribute, 
                         self.command.default_attribute)
        
    def test_args(self):
        self.assertEqual(self.command.args, [])
        
    def test_kwargs(self):
        self.assertEqual(self.command.kwargs, {}) 
        
        
class CommandTest_with_attribute_and_arguments(CommandTest):
    
    #Public
    
    def setUp(self):
        self.command = Command(
            ['run', 'attribute', 'arg1,True,kwarg1=1,', 'kwarg2=1.5'])
    
    def test_attribute(self):
        self.assertEqual(self.command.attribute, 'attribute')
        
    def test_args(self):
        self.assertEqual(self.command.args, ['arg1', True])
        
    def test_kwargs(self):
        self.assertEqual(self.command.kwargs, {'kwarg1': 1, 'kwarg2': 1.5})
            
            
class CommandTest_with_list_flag(CommandTest):     
    
    #Public
    
    def setUp(self):
        self.command = Command(['run', 'attribute', '-l'])
                
    def test_attribute(self):
        self.assertEqual(self.command.attribute, 'list')
        
    def test_args(self):
        self.assertEqual(self.command.args, ['attribute'])


class CommandTest_with_info_flag(CommandTest_with_list_flag):     
    
    #Public
    
    def setUp(self):
        self.command = Command(['run', 'attribute', '-i'])
                
    def test_attribute(self):
        self.assertEqual(self.command.attribute, 'info')  


class CommandTest_with_meta_flag(CommandTest_with_list_flag):     
    
    #Public 
    
    def setUp(self):
        self.command = Command(['run', 'attribute', '-m'])
                
    def test_attribute(self):
        self.assertEqual(self.command.attribute, 'meta')