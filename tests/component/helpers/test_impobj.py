import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.helpers.impobj')


class import_object_Test(unittest.TestCase):

    # Tests

    def test(self):
        self.assertIs(
            component.import_object('unittest.mock.Mock'), Mock)

    def test_with_package(self):
        self.assertIs(
            component.import_object('.Mock', package='unittest.mock'), Mock)

    def test_with_name_in_bad_format(self):
        self.assertRaises(ValueError,
            component.import_object, 'unittest')

    def test_with_module_is_not_existent(self):
        self.assertRaises(ImportError,
            component.import_object, 'not_existent.mock.Mock')

    def test_with_name_is_not_existent(self):
        self.assertRaises(AttributeError,
            component.import_object, 'unittest.mock.not_existent')

    def test_with_name_is_object(self):
        self.assertIs(component.import_object(Mock), Mock)
