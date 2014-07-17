import unittest
from run.var.value import ValueVar, Var, ValueTask

class ValueVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(ValueVar, Var))
        self.assertTrue(issubclass(ValueVar, ValueTask))
