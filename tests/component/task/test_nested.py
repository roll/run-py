import unittest
from unittest.mock import Mock
from run.task.nested import NestedTask

class NestedTaskTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}        
        self.MockTask = self._make_mock_task_class()
        self.task = self.MockTask(
            'task', meta_module=None, *self.args, **self.kwargs)
        
    def test___call__(self):
        self.assertEqual(self.task(), 'value')
        self.task.meta_module.task.assert_called_with('arg1', kwarg1='kwarg1')

    def test___call___with_args_and_kwargs(self):
        args = ('arg2',)
        kwargs = {'kwarg2': 'kwarg2'}
        self.assertEqual(self.task(*args, **kwargs), 'value')
        self.task.meta_module.task.assert_called_with(
            'arg1', 'arg2', kwarg1='kwarg1', kwarg2='kwarg2')
        
    #Protected
    
    def _make_mock_task_class(self):
        class MockTask(NestedTask):
            #Public
            meta_module = Mock(
                meta_basedir='.',
                task=Mock(return_value='value'))
        return MockTask