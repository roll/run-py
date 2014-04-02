import unittest
from unittest.mock import Mock
from run.task.nested import NestedTask

class NestedTaskTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.builtin_task = Mock(return_value='builtin_value')
        MockTask = self._make_mock_task_class(self.builtin_task)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.task = MockTask('task', *self.args, meta_module=None, **self.kwargs)
        
    def test_invoke(self):
        self.assertEqual(self.task.invoke(), 'value')
        self.task.meta_module.task.assert_called_with('arg1', kwarg1='kwarg1')

    def test_invoke_with_args_and_kwargs(self):
        args = ('arg2',)
        kwargs = {'kwarg2': 'kwarg2'}
        self.assertEqual(self.task.invoke(*args, **kwargs), 'value')
        self.task.meta_module.task.assert_called_with(
            'arg1', 'arg2', kwarg1='kwarg1', kwarg2='kwarg2')
        
    #Protected
    
    def _make_mock_task_class(self, builtin_task):
        class MockTask(NestedTask):
            #Public
            meta_module = Mock(task=Mock(
                return_value='value',
                meta_builder=Mock(
                    return_value=builtin_task)))
        return MockTask