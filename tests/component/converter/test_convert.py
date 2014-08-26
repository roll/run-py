import unittest
from unittest.mock import Mock
from run.converter.convert import convert

class convert_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.convert = self._make_mock_convert()

    def test(self):
        self.assertEqual(self.convert('object'), 'value')

    def test_cant_convert(self):
        self.convert._converters.pop()
        self.assertRaises(TypeError, self.convert, 'object')

    # Protected

    def _make_mock_convert(self):
        class mock_convert(convert):
            # Protected
            _converters = [
                Mock(side_effect=TypeError()),
                Mock(return_value='value')]
        return mock_convert
