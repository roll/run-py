import unittest
from run.var.render import RenderVar, Var, RenderTask

class RenderVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(RenderVar, Var))
        self.assertTrue(issubclass(RenderVar, RenderTask))
