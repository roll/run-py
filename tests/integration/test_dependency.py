import unittest
from io import StringIO
from unittest.mock import patch
from run import Module, NullTask, require, trigger

#Tests

class DependencyTest(unittest.TestCase):
    
    #Public

    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.stdout = self.patcher.start()
        self.addCleanup(patch.stopall)         
        self.module = MockMainModule(meta_module=None)
        
    def test_list(self):
        self.module.list()
        self.assertEqual(
            self.stdout.getvalue(), 
            'default\n'
            'info\n'
            'list\n'
            'meta\n'
            'task1\n'
            'task2\n'
            'task3\n')


#Fixtures

class MockMainModule(Module):
    
    #Tasks
    
    task1 = NullTask()
    task2 = NullTask()
    task2.require('task1')
    task2.trigger('task1')
    
    @require('task1')
    @trigger('task2')
    def task3(self):
        pass