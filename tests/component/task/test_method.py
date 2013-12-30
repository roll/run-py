import unittest
from run.task.method import MethodTask

#Tests

class MethodTaskTest(unittest.TestCase):

    #Public

    def test(self):
        task = MockMethodTask(mock_method, module=None)
        self.assertEqual(task.meta_signature, 'qualname(module, value)')
        self.assertEqual(task.meta_docstring, 'docstring')
        self.assertEqual(task.complete('value'), 'value')
    
    
#Fixtures

class MockMethodTask(MethodTask):
    
    #Public
    
    meta_qualname = 'qualname'
    

def mock_method(module, value):
    """docstring"""
    return value