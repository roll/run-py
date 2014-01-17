import unittest
from unittest.mock import Mock
from run.var.partial import PartialVar

class PartialVarTest(unittest.TestCase):

    #Public

    def setUp(self):
        MockPartialVar = self._make_mock_partial_var_class()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.var = MockPartialVar(
            'task', *self.args, module=None, **self.kwargs)
        
    def test_retrieve(self):
        self.assertEqual(self.var.retrieve(), 'value')
        self.var.meta_module.task.assert_called_with(
            'arg1', kwarg1='kwarg1')
        
    #Protected
    
    def _make_mock_partial_var_class(self):
        class MockPartialVar(PartialVar):
            #Public
            meta_module = Mock(task=Mock(return_value='value'))
        return MockPartialVar