import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.helpers.copy')


class copy_Test(unittest.TestCase):

    # Tests

    def test(self):
        self.assertEqual(
            component.copy({'key': 'value'}), {'key': 'value'})

    def test_with_object_has_copy(self):
        obj = Mock(__copy__=lambda: 'copy')
        self.assertEqual(
            component.copy(obj), 'copy')

    def test_with_object_has_copy_with_args_and_kwargs(self):
        args = ('arg1',)
        kwargs = {'kwargs1': 'kwarg1'}
        obj = Mock(__copy__=lambda *args, **kwargs: (args, kwargs))
        self.assertEqual(
            component.copy(obj, *args, **kwargs), (args, kwargs))
