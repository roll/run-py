import unittest
from run import Command

class CommandTest(unittest.TestCase):
    
    #Public
    
    def test_argv1(self):
        command = Command([
             'run', '-s', 'server', 'method', 'arg1,arg2,opt1=True,', 'opt2=2'])
        self.assertEqual(command.server, 'server')
        self.assertEqual(command.method, 'method')
        self.assertEqual(command.arguments, ['arg1', 'arg2'])
        self.assertEqual(command.options, {'opt1': True, 'opt2': 2})
    
    def test_argv2(self):
        command = Command([
             'run', '-s', 'server', 'method', '3'])
        self.assertEqual(command.server, 'server')
        self.assertEqual(command.method, 'method')
        self.assertEqual(command.arguments, [3])
        self.assertEqual(command.options, {})        