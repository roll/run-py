import unittest
from importlib import import_module
from unittest.mock import Mock, patch
component = import_module('run.converter.convert')


class convert_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.converters = self.make_converters()
        patch.object(component.settings, 'converters', self.converters).start()

    # Helpers

    def make_converters(self):
        return [Mock(side_effect=TypeError()),
                Mock(return_value='value')]

    # Tests

    def test(self):
        self.assertEqual(component.convert('object'), 'value')

    def test_cant_convert(self):
        self.converters.clear()
        self.assertRaises(TypeError, component.convert, 'object')
