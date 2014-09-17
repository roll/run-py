import unittest
from importlib import import_module
component = import_module('run.library.derived.var')


class DerivedVarTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(component.DerivedVar, component.Var))
        self.assertTrue(issubclass(component.DerivedVar, component.DerivedTask))
