import unittest
from importlib import import_module
component = import_module('run.module.error')


class NotFoundTest(unittest.TestCase):

    # Helpers

    def raise_error(self):
        raise component.ModuleAttributeError()

    # Tests

    def test(self):
        self.assertRaises(component.ModuleAttributeError, self.raise_error)
