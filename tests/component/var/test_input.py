import unittest
from run.var.input import InputVar, Var, InputTask


class InputVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(InputVar, Var))
        self.assertTrue(issubclass(InputVar, InputTask))
