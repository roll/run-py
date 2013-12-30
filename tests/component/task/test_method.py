import unittest
from run.task.method import MethodTask

#Tests

class MethodTaskTest(unittest.TestCase):

    #Public

    def test(self):
        task = MethodTask(mock_method, module=None)
        self.assertEqual(task.meta_signature, '(module, value)')
        self.assertEqual(task.meta_docstring, 'docstring')
        self.assertEqual(task.complete('value'), 'value')
    
    
#Fixtures

def mock_method(module, value):
    """docstring"""
    return value