import unittest
from run.task.method import MethodTask

class FunctionTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockMethodTask = self._make_mock_method_task_class()
        mock_function = self._make_mock_function()
        self.task = MockMethodTask(mock_function, module=None)
        
    def test_complete(self):        
        self.assertEqual(self.task.complete('value'), 'value')
        
    def test_meta_signature(self):
        self.assertEqual(self.task.meta_signature, 'qualname(module, value)')
       
    def test_meta_docstring(self):        
        self.assertEqual(self.task.meta_docstring, 'docstring')
        
    #Protected
    
    def _make_mock_method_task_class(self):
        class MockMethodTask(MethodTask):
            #Public
            meta_qualname = 'qualname'
        return MockMethodTask
    
    def _make_mock_function(self):
        def mock_function(module, value):
            """docstring"""
            return value
        return mock_function    