import unittest
from importlib import import_module
component = import_module('run.library.find.var')


class FindVarTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(component.FindVar, component.Var))
        self.assertTrue(issubclass(component.FindVar, component.FindTask))
