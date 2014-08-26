import unittest
from unittest.mock import Mock
from run.converter.converter import Converter

class ConverterTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Converter = self._make_mock_converter_class()

    def test(self):
        pass

    # Protected

    def _make_mock_converter_class(self):
        class MockConverter(Converter):
            # Protected
            _match = Mock()
            _make = Mock()
        return MockConverter()
