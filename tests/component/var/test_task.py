import unittest
from unittest.mock import Mock
from run.var.task import TaskVar

class PartialVarTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.builtin_task = Mock(return_value='value')        
        MockVar = self._make_mock_var_class(self.builtin_task)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.var = MockVar('task', *self.args, module=None, **self.kwargs)
        
    def test_retrieve(self):
        self.assertEqual(self.var.retrieve(), 'value')
        self.var.meta_module.task.assert_called_with('arg1', kwarg1='kwarg1')
        
    #Protected
    
    def _make_mock_var_class(self, builtin_task):
        class MockVar(TaskVar):
            #Public
            meta_module = Mock(task=Mock(
                return_value='value',
                meta_builder=Mock(
                    return_value=builtin_task)))
        return MockVar