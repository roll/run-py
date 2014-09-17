import unittest
from importlib import import_module
component = import_module('run.var.function')


class FunctionVarTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(
            component.FunctionVar, component.Var))
        self.assertTrue(issubclass(
            component.FunctionVar, component.FunctionTask))
