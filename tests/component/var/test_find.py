import unittest
from run.var.find import FindVar, Var, FindTask


class FindVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(FindVar, Var))
        self.assertTrue(issubclass(FindVar, FindTask))
