import unittest
from abc import ABCMeta
from unittest.mock import Mock, patch
from run.task import metaclass


class TaskMetaclassTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.NullModule = Mock()
        patch.object(metaclass, 'NullModule', self.NullModule).start()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.Prototype = Mock(return_value=Mock(__meta_build__=Mock()))
        self.Metaclass = self._make_mock_metaclass(self.Prototype)
        self.Class = self._make_mock_class(self.Metaclass)

    def test(self):
        self.assertTrue(issubclass(self.Metaclass, ABCMeta))

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
        # Check NullModule call
        self.NullModule.assert_called_with()
        # Check prototype call
        self.prototype = self.Prototype.return_value
        self.prototype.__meta_build__.assert_called_with(
            self.NullModule.return_value)

    # Protected

    def _make_mock_metaclass(self, Prototype):
        class MockMetaclass(metaclass.TaskMetaclass):
            # Protected
            _meta_TaskPrototype = Prototype
        return MockMetaclass

    def _make_mock_class(self, mock_metaclass):
            class MockClass(metaclass=mock_metaclass): pass
            return MockClass
