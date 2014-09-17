import unittest
from importlib import import_module
component = import_module('run.library.find.not_found')


class NotFoundTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(component.NotFound, Exception))