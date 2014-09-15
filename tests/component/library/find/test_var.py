import unittest
from run.library.find import var


class FindVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(var.FindVar, var.Var))
        self.assertTrue(issubclass(var.FindVar, var.FindTask))
