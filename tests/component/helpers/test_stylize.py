import unittest
from functools import partial
from importlib import import_module
component = import_module('run.helpers.stylize')


class stylize_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.pstylize = partial(component.stylize, 'test')

    # Tests

    def test_1(self):
        result = self.pstylize(bold=True)
        self.assertEqual(result, '\x1b[1mtest\x1b[0m')

    def test_2(self):
        result = self.pstylize(foreground='red')
        self.assertEqual(result, '\x1b[31mtest\x1b[0m')

    def test_with_error(self):
        self.assertRaises(ValueError, self.pstylize, error='error')
