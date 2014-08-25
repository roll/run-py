import unittest
from unittest.mock import Mock
from run.var.var import Var


class VarTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Var = self._make_mock_var_class()
        self.var = self.Var(meta_module=None)

    def test_meta_signature(self):
        self.assertEqual(self.var.meta_signature, '')

    # Protected

    def _make_mock_var_class(self):
        class MockVar(Var):
            # Public
            meta_invoke = Mock(return_value='value')
            meta_dispatcher = Mock()
            # Protected
            _meta_TaskSignal = Mock(return_value='signal')
        return MockVar
