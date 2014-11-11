import unittest
from unittest.mock import Mock
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

    def test_meta_cache(self):
        self.assertEqual(self.var.meta_cache, component.settings.cache)

    def test_meta_signature(self):
        self.assertEqual(self.var.meta_signature, '')

    def test_meta_style(self):
        self.assertEqual(self.var.meta_style, 'var')
