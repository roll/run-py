import unittest
from run.var.descriptor import DescriptorVar, Var, DescriptorTask


class DescriptorVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(DescriptorVar, Var))
        self.assertTrue(issubclass(DescriptorVar, DescriptorTask))
