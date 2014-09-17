import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.converter.converter')


class ConverterTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.converter = self.make_mock_converter()

    # Helpers

    def make_mock_converter(self):
        class mock_converter(component.Converter):
            # Protected
            _match = Mock()
            _make = Mock()
        return mock_converter

    # Tests

    def test(self):
        self.assertEqual(
            self.converter(**self.kwargs)('object'),
            self.converter._make.return_value)

    def test_with_kwargs(self):
        self.assertEqual(
            self.converter('object'),
            self.converter._make.return_value)

    def test_with_converted_object(self):
        result = component.Result()
        self.assertEqual(self.converter(result), result)

    def test_with_staticmethod_object(self):
        self.assertRaises(TypeError, self.converter, staticmethod(print))

    def test_with_classmethod_object(self):
        self.assertRaises(TypeError, self.converter, classmethod(print))

    def test_with_skipped_object(self):
        self.assertRaises(TypeError, self.converter, component.skip(Mock()))
