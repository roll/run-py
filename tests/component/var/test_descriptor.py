import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.var.descriptor')


class DescriptorVarTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.descriptor = Mock(__get__=Mock(), __doc__='__doc__')
        self.var = component.DescriptorVar(self.descriptor, Build=True)

    # Tests

    def test___call__(self):
        result = self.var()
        self.assertEqual(result, self.descriptor.__get__.return_value)
        self.descriptor.__get__.assert_called_with(
            self.var.Module, type(self.var.Module))

    def test_Docstring(self):
        self.assertEqual(self.var.Docstring, self.descriptor.__doc__)
