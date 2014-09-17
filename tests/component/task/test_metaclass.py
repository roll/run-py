import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.metaclass')


@unittest.skip
class TaskMetaclassTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.Prototype = Mock(return_value=Mock(__meta_build__=Mock()))
        self.Class = self.make_mock_class(self.Prototype)

    # Helpers

    def make_mock_class(self, Prototype):
        class MockClass(metaclass=component.TaskMetaclass):
            # Public
            meta_prototype = Prototype
        return MockClass

    # Tests

    def test___call__(self):
        instance = self.Class(*self.args, **self.kwargs)
        self.assertIsInstance(instance, Mock)
        # Check Prototype call
        self.Prototype.assert_called_with(
            *self.args,
            meta_class=self.Class,
            meta_updates=None,
            **self.kwargs)
        # Check prototype call
        self.assertFalse(self.Prototype.return_value.called)

    def test___call___with_module(self):
        instance = self.Class(meta_module='module')
        self.assertIsInstance(instance, Mock)
        # Check Prototype call
        self.Prototype.assert_called_with(
            meta_class=self.Class,
            meta_updates=None)
        # Check prototype call
        self.prototype = self.Prototype.return_value
        self.prototype.__meta_build__.assert_called_with('module')

    def test___call___with_module_is_none(self):
        instance = self.Class(meta_module=None)
        self.assertIsInstance(instance, Mock)
        # Check Prototype call
        self.Prototype.assert_called_with(
            meta_class=self.Class,
            meta_updates=None)
        # Check prototype call
        self.prototype = self.Prototype.return_value
        self.prototype.__meta_build__.assert_called_with(None)
