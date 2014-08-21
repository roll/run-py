import unittest
from unittest.mock import Mock, call, patch
from run.var.var import Var


class VarTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Var = self._make_mock_var_class()
        self.var = self.Var(meta_module=None, meta_cache=True)
        self.addCleanup(patch.stopall)

    # TODO: move to Task
    def test___get__(self):
        self.assertEqual(self.var.__get__('module'), 'value')
        self.assertEqual(self.var.__get__('module'), 'value')
        # Only one call because of caching
        self.assertEqual(self.var.meta_invoke.call_count, 1)
        self.var.meta_invoke.assert_called_with()
        # Check TaskSignal call
        self.var._meta_OperationSignal.assert_has_calls(
            [call(operation=self.var, event='initiated'),
             call(operation=self.var, event='successed')])
        # Check dispatcher.add_signal call
        self.var.meta_dispatcher.add_signal.assert_has_calls(
            [call('signal'), call('signal')])

    def test___get___with_meta_cache_is_false(self):
        self.var.meta_cache = False
        self.assertEqual(self.var.__get__('module'), 'value')
        self.assertEqual(self.var.__get__('module'), 'value')
        # Two calls because of caching is off
        self.assertEqual(self.var.meta_invoke.call_count, 2)

    def test_meta_signature(self):
        self.assertEqual(self.var.meta_signature, '')

    # Protected

    def _make_mock_var_class(self):
        class MockVar(Var):
            # Public
            meta_invoke = Mock(return_value='value')
            meta_dispatcher = Mock()
            # Protected
            _meta_OperationSignal = Mock(return_value='signal')
        return MockVar
