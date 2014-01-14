import unittest
from unittest.mock import Mock
from run.task.partial import PartialTask

class PartialTaskTest(unittest.TestCase):

    #Public

    def setUp(self):
        MockPartialTask = self._make_mock_partial_task_class()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.task = MockPartialTask(
            'task', *self.args, module=None, **self.kwargs)
        
    def test_complete(self):
        self.assertEqual(self.task.complete(), 'value')
        self.task.meta_module.task.assert_called_with(
            'arg1', kwarg1='kwarg1')

    def test_complete_with_args_and_kwargs(self):
        args = ('arg2',)
        kwargs = {'kwarg2': 'kwarg2'}
        self.assertEqual(self.task.complete(*args, **kwargs), 'value')
        self.task.meta_module.task.assert_called_with(
            'arg1', 'arg2', kwarg1='kwarg1', kwarg2='kwarg2')
        
    #Protected
    
    def _make_mock_partial_task_class(self):
        class MockPartialTask(PartialTask):
            #Public
            meta_module = Mock(task=Mock(return_value='value'))
        return MockPartialTask