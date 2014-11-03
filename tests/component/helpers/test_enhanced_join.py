import os
import unittest
from unittest.mock import patch
from importlib import import_module
component = import_module('run.helpers.enhanced_join')


class enhanced_join_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        patch('os.path.sep', new='/').start()
        self.addCleanup(patch.stopall)
        self.error = os.error()

    # Tests

    def test(self):
        self.assertEqual(component.enhanced_join('x', 'y'), 'x/y')

    def test_with_none(self):
        self.assertEqual(component.enhanced_join('x', None), 'x')

    def test_with_error(self):
        self.assertRaises(Exception, component.enhanced_join)

    def test_with_error_and_fallback(self):
        self.assertEqual(component.enhanced_join(fallback='fallback'), 'fallback')
