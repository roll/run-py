import unittest
from run.library.derived.var import DerivedTask, DerivedVar, Var


class DerivedVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(DerivedVar, Var))
        self.assertTrue(issubclass(DerivedVar, DerivedTask))
