import unittest
from importlib import import_module
component = import_module('run.module.exception')


class NotFoundTest(unittest.TestCase):

    # Helpers

    def raise_error(self):
        raise component.GetattrError()

    # Tests

    def test(self):
        self.assertRaises(component.GetattrError, self.raise_error)
