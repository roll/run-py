import unittest
from unittest.mock import Mock
from run.var.method import MethodVar

class MethodTaskTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.function = Mock(return_value='value')
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}         
        self.var = MethodVar(
            self.function, *self.args, module='module', **self.kwargs)       
        
    def test_invoke(self):        
        self.assertEqual(self.var.invoke(), 'value')
        self.function.assert_called_with('module', *self.args, **self.kwargs)