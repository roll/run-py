import unittest
from unittest.mock import Mock
from run.frame.converter.converter import Converter, Result, skip

class ConverterTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.converter = self._make_mock_converter()

    def test(self):
        self.assertEqual(
            self.converter(**self.kwargs)('object'),
            self.converter._make.return_value)

    def test_with_kwargs(self):
        self.assertEqual(
            self.converter('object'),
            self.converter._make.return_value)

    def test_with_converted_object(self):
        result = Result()
        self.assertEqual(self.converter(result), result)

    def test_with_staticmethod_object(self):
        self.assertRaises(TypeError, self.converter, staticmethod(print))

    def test_with_classmethod_object(self):
        self.assertRaises(TypeError, self.converter, classmethod(print))

    def test_with_skipped_object(self):
        self.assertRaises(TypeError, self.converter, skip(Mock()))

    # Protected

    def _make_mock_converter(self):
        class mock_converter(Converter):
            # Protected
            _match = Mock()
            _make = Mock()
        return mock_converter
