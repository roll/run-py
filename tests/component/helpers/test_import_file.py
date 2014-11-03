import os
import unittest
from importlib import import_module
component = import_module('run.helpers.import_file')


class import_file_Test(unittest.TestCase):

    # Tests

    def test(self):
        filepath = os.path.join(os.path.dirname(__file__), 'test_enhanced_copy.py')
        module = component.import_file(filepath)
        self.assertIs(module.unittest, unittest)