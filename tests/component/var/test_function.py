import unittest
from unittest.mock import Mock
from run.var.function import FunctionVar

class FunctionTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.function = Mock(return_value='value', __doc__='docstring')        
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.var = FunctionVar(
            self.function, *self.args, module=None, **self.kwargs)
        
    def test_invoke(self):        
        self.assertEqual(self.var.invoke(), 'value')
        self.function.assert_called_with(*self.args, **self.kwargs)
       
    def test_meta_docstring(self):        
        self.assertEqual(self.var.meta_docstring, 'docstring')