import unittest
from importlib import import_module
component = import_module('run.library.value.task')


class ValueTaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.task = component.ValueTask('value', meta_module=None)

    # Tests

    def test___call__(self):
        self.assertEqual(self.task(), 'value')
