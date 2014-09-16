import unittest
from unittest.mock import Mock, patch
from run.converter.convert import convert, settings

class convert_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.converters = self._make_converters()
        patch.object(settings, 'converters', self.converters).start()

    def test(self):
        self.assertEqual(convert('object'), 'value')

    def test_cant_convert(self):
        self.converters.clear()
        self.assertRaises(TypeError, convert, 'object')

    # Protected

    def _make_converters(self):
        return [Mock(side_effect=TypeError()),
                Mock(return_value='value')]
