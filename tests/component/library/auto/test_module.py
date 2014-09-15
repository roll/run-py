import unittest
import fractions
from functools import partial
from run.library.auto.module import AutoModule


class AutoModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.pModule = partial(AutoModule, meta_module=None)
        self.module = self.pModule([fractions])

    def test_gcd(self):
        self.assertEqual(self.module.gcd(10, 15), 5)

    def test_meta_docstring(self):
        self.assertTrue(self.module.meta_docstring)

    def test_meta_tasks(self):
        self.assertEqual(sorted(self.module.meta_tasks),
            ['gcd', 'info', 'list', 'meta'])

    def test_meta_tasks_witout_sources(self):
        self.module = self.pModule()
        self.assertEqual(sorted(self.module.meta_tasks),
            ['info', 'list', 'meta'])
