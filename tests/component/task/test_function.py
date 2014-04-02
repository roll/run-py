import unittest
from unittest.mock import Mock
from run.task.function import FunctionTask

class FunctionTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockFunctionTask = self._make_mock_function_task_class()
        self.function = Mock(return_value='value', __doc__='docstring')        
        self.task = MockFunctionTask(self.function, meta_module=None)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}        
        
    def test_invoke(self):        
        self.assertEqual(self.task.invoke(*self.args, **self.kwargs), 'value')
        self.function.assert_called_with(*self.args, **self.kwargs)
        
    def test_meta_signature(self):
        self.assertEqual(self.task.meta_signature, 'qualname(*args, **kwargs)')
       
    def test_meta_docstring(self):        
        self.assertEqual(self.task.meta_docstring, 'docstring')
        
    #Protected
    
    def _make_mock_function_task_class(self):
        class MockFunctionTask(FunctionTask):
            #Public
            meta_qualname = 'qualname'
        return MockFunctionTask 