import unittest
from run.var.function import FunctionVar, Var, FunctionTask

class FunctionVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(FunctionVar, Var))
        self.assertTrue(issubclass(FunctionVar, FunctionTask))
