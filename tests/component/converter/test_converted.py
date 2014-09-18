import unittest
from importlib import import_module
component = import_module('run.converter.converted')


class ConvertedTest(unittest.TestCase):

    # Tests

    def test(self):
        self.assertTrue(issubclass(component.Converted, object))