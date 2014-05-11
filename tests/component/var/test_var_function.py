import unittest
from unittest.mock import Mock, patch
from run.var.var_function import var

class var_Test(unittest.TestCase):

    #Public

    def setUp(self):
        self.method = 'method'
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.property = Mock(return_value='property')
        self.task_class = Mock(return_value='var')
        patch('builtins.property', new=self.property).start()       
        patch.object(var, '_task_class', new=self.task_class).start()
        self.addCleanup(patch.stopall)

    def test_as_function(self):
        self.assertEqual(var(self.method, **self.kwargs), 'var')
        self.property.assert_called_with(self.method)
        self.task_class.assert_called_with('property', **self.kwargs)
        
    def test_as_decorator(self):
        self.assertEqual(var(**self.kwargs)('method'), 'var')
        self.property.assert_called_with(self.method)
        self.task_class.assert_called_with('property', **self.kwargs) 