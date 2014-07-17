import unittest
from run.var.null import NullVar, Var, NullTask

class NullVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(NullVar, Var))
        self.assertTrue(issubclass(NullVar, NullTask))
