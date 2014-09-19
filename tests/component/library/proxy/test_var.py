import unittest
from importlib import import_module
component = import_module('run.library.proxy.var')


class ProxyVarTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(component.ProxyVar, component.Var))
        self.assertTrue(issubclass(component.ProxyVar, component.ProxyTask))
