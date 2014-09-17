import unittest
from importlib import import_module
component = import_module('run.library.dialog.var')


class DialogVarTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(component.DialogVar, component.Var))
        self.assertTrue(issubclass(component.DialogVar, component.DialogTask))
