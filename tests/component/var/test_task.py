import unittest
from unittest.mock import Mock
from run.var.task import TaskVar

class PartialVarTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.base_task = Mock(return_value='value')        
        MockVar = self._make_mock_var_class(self.base_task)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.var = MockVar('task', *self.args, module=None, **self.kwargs)
        
    def test_retrieve(self):
        self.assertEqual(self.var.retrieve(), 'value')
        self.base_task.assert_called_with('arg1', kwarg1='kwarg1')
        
    #Protected
    
    def _make_mock_var_class(self, base_task):
        class MockVar(TaskVar):
            #Public
            meta_module = Mock(meta_attributes={
                'task': Mock(meta_builder=Mock(return_value=base_task))})
        return MockVar