import unittest
from functools import partial
from importlib import import_module
component = import_module('run.utils.stylize')


class stylize_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.stylize = partial(component.stylize, 'test')

    # Tests

    def test(self):
        result = self.stylize(styles=['done'], bold=True)
        self.assertEqual(result, '\x1b[1;92mtest\x1b[0m')
