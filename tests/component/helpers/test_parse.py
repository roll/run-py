import unittest
from importlib import import_module
component = import_module('run.helpers.parse')


class parse_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.parse = component.parse

    # Tests

    def test(self):
        self.assertEqual(self.parse('1'), ((1,), {}))
        self.assertEqual(self.parse('a=1'), ((), {'a': 1}))
        self.assertEqual(self.parse('1, a=1'), ((1,), {'a': 1}))
        self.assertEqual(self.parse('"1", a=1'), (('1',), {'a': 1}))
