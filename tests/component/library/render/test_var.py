import unittest
from run.library.render import var


class RenderVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(var.RenderVar, var.Var))
        self.assertTrue(issubclass(var.RenderVar, var.RenderTask))
