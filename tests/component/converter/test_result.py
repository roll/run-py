import unittest
from importlib import import_module
component = import_module('run.converter.result')


class ResultTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(component.Result, object))