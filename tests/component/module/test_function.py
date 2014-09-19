import unittest
import fractions
from functools import partial
from importlib import import_module
component = import_module('run.module.function')


class FunctionModuleTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.pModule = partial(component.FunctionModule, meta_module=None)
        self.module = self.pModule(fractions)

    # Tests

    def test_gcd(self):
        self.assertEqual(self.module.gcd(10, 15), 5)

    def test_meta_docstring(self):
        self.assertTrue(self.module.meta_docstring)

    def test_meta_tasks(self):
        self.assertEqual(sorted(self.module.meta_tasks),
            ['gcd', 'info', 'list', 'meta'])
