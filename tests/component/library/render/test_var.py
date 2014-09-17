import unittest
from importlib import import_module
component = import_module('run.library.render.var')


class RenderVarTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(component.RenderVar, component.Var))
        self.assertTrue(issubclass(component.RenderVar, component.RenderTask))
