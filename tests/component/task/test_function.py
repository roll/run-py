import unittest
from unittest.mock import Mock
from run.task.function import FunctionTask

class FunctionTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'} 
        self.function = Mock(__doc__='__doc__')        
        self.task = FunctionTask(self.function, meta_module=None)
        
    def test___call__(self):
        result = self.task(*self.args, **self.kwargs)  
        self.assertEqual(result, self.function.return_value)
        self.function.assert_called_with(*self.args, **self.kwargs)
        
    def test_meta_signature(self):
        self.assertEqual(self.task.meta_signature, '(*args, **kwargs)')
       
    def test_meta_docstring(self):        
        self.assertEqual(self.task.meta_docstring, self.function.__doc__)