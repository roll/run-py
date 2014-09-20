import unittest
from unittest.mock import Mock, ANY
from importlib import import_module
component = import_module('run.library.find.find_modules')


@unittest.skip
class find_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.find = self.make_mock_find()

    # Helpers

    def make_mock_find(self):
        class mock_find(component.find_modules):
            # Public
            default_basedir = 'default_basedir'
            default_exclude = 'default_exclude'
            default_file = 'default_file'
            default_key = 'default_key'
            default_recursively = 'default_recursively'
            default_tags = 'default_tags'
            default_target = 'default_target'
            # Protected
            _find_objects = Mock()
        return mock_find

    # Tests

    def test(self):
        result = self.find()
        self.assertEqual(result, self.find._find_objects.return_value)
        # Check find_objects call
        self.find._find_objects.assert_called_with(
            basedir='default_basedir',
            filepathes=None,
            filters=[
                {'filename': 'default_file'},
                {'notfilename': 'default_exclude'}],
            constraints=ANY,
            getfirst_exception=self.find._getfirst_exception)

    def test_with_recursively_is_false(self):
        result = self.find(recursively=False)
        self.assertEqual(result, self.find._find_objects.return_value)
        # Check find_objects call
        self.find._find_objects.assert_called_with(
            basedir='default_basedir',
            filepathes=None,
            filters=[
                {'filename': 'default_file'},
                {'maxdepth': 1},
                {'notfilename': 'default_exclude'}],
            constraints=ANY,
            getfirst_exception=self.find._getfirst_exception)

    def test_with_file_is_filepath(self):
        result = self.find(file='dir/file')
        self.assertEqual(result, self.find._find_objects.return_value)
        # Check find_objects call
        self.find._find_objects.assert_called_with(
            basedir='default_basedir',
            filepathes=['dir/file'],
            filters=[
                {'notfilename': 'default_exclude'}],
            constraints=ANY,
            getfirst_exception=self.find._getfirst_exception)

    def test_with_file_is_filepath_and_recursively_is_false(self):
        result = self.find(file='dir/file', recursively=False)
        self.assertEqual(result, self.find._find_objects.return_value)
        # Check find_objects call
        self.find._find_objects.assert_called_with(
            basedir='default_basedir',
            filepathes=['dir/file'],
            filters=[
                {'notfilename': 'default_exclude'}],
            constraints=ANY,
            getfirst_exception=self.find._getfirst_exception)

    def test_with_exclude_is_filepath(self):
        result = self.find(exclude='dir/file')
        self.assertEqual(result, self.find._find_objects.return_value)
        # Check find_objects call
        self.find._find_objects.assert_called_with(
            basedir='default_basedir',
            filepathes=None,
            filters=[
                {'filename': 'default_file'},
                {'notfilepath': 'dir/file'}],
            constraints=ANY,
            getfirst_exception=self.find._getfirst_exception)
