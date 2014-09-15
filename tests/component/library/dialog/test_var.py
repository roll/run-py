import unittest
from run.library.dialog import var


class DialogVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(var.DialogVar, var.Var))
        self.assertTrue(issubclass(var.DialogVar, var.DialogTask))
