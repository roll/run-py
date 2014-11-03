import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.var.descriptor')


class DescriptorVarTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.descriptor = Mock(__get__=Mock(), __doc__='__doc__')
        self.var = component.DescriptorVar(self.descriptor, meta_module=None)

    # Tests

    def test___call__(self):
        result = self.var()
        self.assertEqual(result, self.descriptor.__get__.return_value)
        self.descriptor.__get__.assert_called_with(
            self.var.meta_module, type(self.var.meta_module))

    def test_meta_docstring(self):
        self.assertEqual(self.var.meta_docstring, self.descriptor.__doc__)
