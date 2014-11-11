import unittest
from unittest.mock import Mock, patch, call
from importlib import import_module
component = import_module('run.var.var')


class VarTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.Var = self.make_mock_var_class()
        self.var = self.Var(meta_build=True)

    # Helpers

    def make_mock_var_class(self):
        class MockVar(component.Var):
            # Public
            meta_invoke = Mock(return_value='value')
        return MockVar

    # Tests

    def test___get___(self):
        self.Var.meta_cache = False
        self.assertEqual(self.var.__get__('module'), 'value')
        self.assertEqual(self.var.__get__('module'), 'value')
        # Two calls because of caching is off
        self.assertEqual(self.var.meta_invoke.call_count, 2)

    @unittest.skip
    @patch.object(component, 'TaskEvent')
    def test___get___with_meta_cache_is_true(self, TaskEvent):
        self.Task.meta_is_descriptor = True
        self.Task.meta_cache = True
        self.Task.meta_dispatcher = Mock()
        self.assertEqual(self.task.__get__('module'), 'value')
        self.assertEqual(self.task.__get__('module'), 'value')
        # Only one call because of caching
        self.assertEqual(self.task.meta_invoke.call_count, 1)
        self.task.meta_invoke.assert_called_with(*self.args, **self.kwargs)
        # Check TaskEvent call
        TaskEvent.assert_has_calls(
            [call(self.task, event='called'),
             call(self.task, event='successed')])
        # Check dispatcher.add_event call
        self.task.meta_dispatcher.add_event.assert_has_calls(
            [call(TaskEvent.return_value),
             call(TaskEvent.return_value)])

    def test_meta_cache(self):
        self.assertEqual(self.var.meta_cache, component.settings.cache)

    def test_meta_signature(self):
        self.assertEqual(self.var.meta_signature, '')

    def test_meta_style(self):
        self.assertEqual(self.var.meta_style, 'var')
