import unittest
from run.var.subprocess import SubprocessVar, Var, SubprocessTask


class SubprocessVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(SubprocessVar, Var))
        self.assertTrue(issubclass(SubprocessVar, SubprocessTask))
