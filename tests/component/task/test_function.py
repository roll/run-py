import unittest
from run.task.function import FunctionTask

#Tests

class FunctionTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.task = MockFunctionTask(mock_function, module=None)
        
    def test_complete(self):        
        self.assertEqual(self.task.complete('value'), 'value')
        
    def test_meta_signature(self):
        self.assertEqual(self.task.meta_signature, 'qualname(module, value)')
       
    def test_meta_docstring(self):        
        self.assertEqual(self.task.meta_docstring, 'docstring')
    
    
#Fixtures

class MockFunctionTask(FunctionTask):
    
    #Public
    
    meta_qualname = 'qualname'
    

def mock_function(module, value):
    """docstring"""
    return value