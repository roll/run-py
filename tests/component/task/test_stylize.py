import unittest
from functools import partial
from importlib import import_module
component = import_module('run.task.stylize')


class stylize_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.pstylize = partial(component.stylize, 'test')

    # Tests

    def test(self):
        result = self.pstylize(style='done', bold=True)
        self.assertEqual(result, '\x1b[1;92mtest\x1b[0m')

    def test_with_style_is_dict(self):
        result = self.pstylize(style={'foreground': 'bright_green'}, bold=True)
        self.assertEqual(result, '\x1b[1;92mtest\x1b[0m')
