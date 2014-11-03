import os
import unittest
from importlib import import_module
component = import_module('run.helpers.load')


class load_Test(unittest.TestCase):

    # Tests

    def test(self):
        filepath = os.path.join(os.path.dirname(__file__), 'test_copy.py')
        module = component.load(filepath)
        self.assertIs(module.unittest, unittest)