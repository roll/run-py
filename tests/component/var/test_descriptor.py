import unittest
from importlib import import_module
component = import_module('run.var.descriptor')


class DescriptorVarTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(
            component.DescriptorVar, component.Var))
        self.assertTrue(issubclass(
            component.DescriptorVar, component.DescriptorTask))
