import unittest
from unittest.mock import Mock
from run.var.task import TaskVar

class PartialVarTest(unittest.TestCase):

    #Public

    def setUp(self):
        MockTaskVar = self._make_mock_task_var_class()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.var = MockTaskVar(
            'task', *self.args, module=None, **self.kwargs)
        
    def test_retrieve(self):
        self.assertEqual(self.var.retrieve(), 'value')
        self.var.meta_module.task.assert_called_with(
            'arg1', kwarg1='kwarg1')
        
    #Protected
    
    def _make_mock_task_var_class(self):
        class MockTaskVar(TaskVar):
            #Public
            meta_module = Mock(task=Mock(return_value='value'))
        return MockTaskVar