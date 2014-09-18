import unittest
from unittest.mock import Mock, patch
from importlib import import_module
component = import_module('run.task.prototype')


class PrototypeTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.update = Mock()
        self.Update = Mock(return_value=self.update)
        patch.object(component, 'Update', self.Update).start()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.Task = self.make_mock_task_class()
        self.prototype = component.Prototype(
            *self.args, meta_class=self.Task, **self.kwargs)

    # Helpers

    def make_mock_task_class(self):
        class MockTask:
            # Public
            __meta_create__ = Mock()
            __meta_update__ = Mock()
            attr1 = 'value1'
            attr2 = Mock
        return MockTask

    # Tests

    def test___getattr__(self):
        self.assertEqual(self.prototype.attr2, Mock)

    def test___setattr__(self):
        self.prototype.attr3.nested_attr3 = 'value2'
        # Check update_class call
        self.Update.assert_called_with(
            '__setattr__', 'attr3.nested_attr3', 'value2')

    def test___call__(self):
        self.prototype.attr3.nested_attr3(*self.args, **self.kwargs)
        # Check update_class call
        self.Update.assert_called_with(
            'attr3.nested_attr3', *self.args, **self.kwargs)

    def test___call___before_getattr(self):
        self.assertRaises(TypeError, self.prototype)

    def test_meta_fork(self):
        self.prototype.attr2 = 'value2'
        fork = self.prototype.meta_fork('arg2', kwarg2='kwarg2')
        self.assertIsInstance(fork, component.Prototype)

    # TODO: implement
    def test_meta_build(self):
        pass
