import unittest
from unittest.mock import Mock, patch, call
from importlib import import_module
component = import_module('run.var.var')


class VarTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.Var = self.make_mock_var_class()
        self.var = self.Var(Build=True)

    # Helpers

    def make_mock_var_class(self):
        class MockVar(component.Var):
            # Public
            Invoke = Mock(return_value='value')
        return MockVar

    # Tests

    def test___get___(self):
        self.Var.Cache = False
        self.assertEqual(self.var.__get__('module'), 'value')
        self.assertEqual(self.var.__get__('module'), 'value')
        # Two calls because of caching is off
        self.assertEqual(self.var.Invoke.call_count, 2)

    @unittest.skip
    @patch.object(component, 'TaskEvent')
    def test___get___with_Cache_is_true(self, TaskEvent):
        self.Task.IsDescriptor = True
        self.Task.Cache = True
        self.Task.Dispatcher = Mock()
        self.assertEqual(self.task.__get__('module'), 'value')
        self.assertEqual(self.task.__get__('module'), 'value')
        # Only one call because of caching
        self.assertEqual(self.task.Invoke.call_count, 1)
        self.task.Invoke.assert_called_with(*self.args, **self.kwargs)
        # Check TaskEvent call
        TaskEvent.assert_has_calls(
            [call(self.task, event='called'),
             call(self.task, event='successed')])
        # Check dispatcher.add_event call
        self.task.Dispatcher.add_event.assert_has_calls(
            [call(TaskEvent.return_value),
             call(TaskEvent.return_value)])

    def test_Cache(self):
        self.assertEqual(self.var.Cache, component.settings.cache)

    def test_Signature(self):
        self.assertEqual(self.var.Signature, '')

    def test_Style(self):
        self.assertEqual(self.var.Style, 'var')
