import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.var.var')


class VarTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.Var = self.make_mock_var_class()
        self.var = self.Var(meta_module=None)

    # Helpers

    def make_mock_var_class(self):
        class MockVar(component.Var):
            # Public
            meta_invoke = Mock(return_value='value')
            meta_dispatcher = Mock()
        return MockVar

    # Tests

    def test_meta_is_descriptor(self):
        self.assertEqual(self.var.meta_is_descriptor, True)

    def test_meta_signature(self):
        self.assertEqual(self.var.meta_signature, '')

    def test_meta_style(self):
        self.assertEqual(self.var.meta_style, 'var')
