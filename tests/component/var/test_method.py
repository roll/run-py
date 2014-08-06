import unittest
from run.var.method import MethodVar, Var, MethodTask


class MethodVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(MethodVar, Var))
        self.assertTrue(issubclass(MethodVar, MethodTask))
