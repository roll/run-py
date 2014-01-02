import unittest
from run.task.method import MethodTask

#Tests

class MethodTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.task = MockMethodTask(mock_method, module=None)
        
    def test_complete(self):        
        self.assertEqual(self.task.complete('value'), 'value')
        
    def test_meta_signature(self):
        self.assertEqual(self.task.meta_signature, 'qualname(module, value)')
       
    def test_meta_docstring(self):        
        self.assertEqual(self.task.meta_docstring, 'docstring')
    
    
#Fixtures

class MockMethodTask(MethodTask):
    
    #Public
    
    meta_qualname = 'qualname'
    

def mock_method(module, value):
    """docstring"""
    return value