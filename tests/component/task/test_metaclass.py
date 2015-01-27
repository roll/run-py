import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.metaclass')


@unittest.skip
class MetaclassTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.Prototype = Mock(return_value=Mock(__Build__=Mock()))
        self.Class = self.make_mock_class(self.Prototype)

    # Helpers

    def make_mock_class(self, Prototype):
        class MockClass(metaclass=component.Metaclass):
            # Public
            Prototype = Prototype
        return MockClass

    # Tests

    def test___call__(self):
        instance = self.Class(*self.args, **self.kwargs)
        self.assertIsInstance(instance, Mock)
        # Check Prototype call
        self.Prototype.assert_called_with(
            *self.args,
            Class=self.Class,
            Updates=None,
            **self.kwargs)
        # Check prototype call
        self.assertFalse(self.Prototype.return_value.called)

    def test___call___with_module(self):
        instance = self.Class(Build=True, Module='module')
        self.assertIsInstance(instance, Mock)
        # Check Prototype call
        self.Prototype.assert_called_with(
            Class=self.Class,
            Updates=None)
        # Check prototype call
        self.prototype = self.Prototype.return_value
        self.prototype.__Build__.assert_called_with('module')

    def test___call___with_module_is_none(self):
        instance = self.Class(Build=True)
        self.assertIsInstance(instance, Mock)
        # Check Prototype call
        self.Prototype.assert_called_with(
            Class=self.Class,
            Updates=None)
        # Check prototype call
        self.prototype = self.Prototype.return_value
        self.prototype.__Build__.assert_called_with(None)
