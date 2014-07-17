import unittest
from run.var.derived import DerivedVar, Var, DerivedTask

class DerivedVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(DerivedVar, Var))
        self.assertTrue(issubclass(DerivedVar, DerivedTask))
