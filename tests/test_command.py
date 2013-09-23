import unittest
from run import Command

class CommandTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.command = Command(
            ['run', '-s', 'server', 'method', 'arg1,arg2,opt1=True'])
    
    def test_method(self):
        self.assertEqual(self.command.method, 'method')
    
    def test_arguments(self):
        self.assertEqual(self.command.arguments, ['arg1', 'arg2'])
    
    def test_options(self):
        self.assertEqual(self.command.options, {'opt1': True})