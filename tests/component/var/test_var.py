import unittest
from unittest.mock import Mock, call, patch
from run.var.var import Var

class VarTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Var = self._make_MockVar()
        self.var = self.Var(meta_module=None)
        patch('run.NullModule.meta_cache', True).start()
        self.addCleanup(patch.stopall)

    def test___get__(self):
        self.assertEqual(self.var.__get__('module'), 'value')
        self.assertEqual(self.var.__get__('module'), 'value')
        # Only one call because of caching
        self.assertEqual(self.var.meta_invoke.call_count, 1)
        self.var.meta_invoke.assert_called_with()
        self.var._meta_InitiatedTaskSignal.assert_called_with(self.var)
        self.var._meta_SuccessedTaskSignal.assert_called_with(self.var)
        self.var.meta_dispatcher.add_signal.assert_has_calls(
            [call('initiated_signal'),
             call('successed_signal')])

    def test___get___with_meta_cache_is_false(self):
        self.var.meta_cache = False
        self.assertEqual(self.var.__get__('module'), 'value')
        self.assertEqual(self.var.__get__('module'), 'value')
        # Two calls because of caching is off
        self.assertEqual(self.var.meta_invoke.call_count, 2)

    def test_meta_cache(self):
        self.assertEqual(self.var.meta_cache, True)
        self.var.meta_cache = False
        self.assertEqual(self.var.meta_cache, False)

    def test_meta_signature(self):
        self.assertEqual(self.var.meta_signature, '')

    # Protected

    def _make_MockVar(self):
        class MockVar(Var):
            # Public
            meta_invoke = Mock(return_value='value')
            meta_dispatcher = Mock()
            # Protected
            _meta_InitiatedTaskSignal = Mock(return_value='initiated_signal')
            _meta_SuccessedTaskSignal = Mock(return_value='successed_signal')
        return MockVar
