import unittest
from unittest.mock import Mock
from run.task.prototype import TaskPrototype

class TaskPrototypeTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.update = Mock()
        self.updates = []
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.Attribute = self._make_mock_attribute_class()
        self.Prototype = self._make_mock_prototype_class(self.update)
        self.prototype = self.Prototype(
            self.Attribute, self.updates, *self.args, **self.kwargs)

    def test___getattr___no_attribute(self):
        self.assertRaises(AttributeError, getattr, self.prototype , 'attr2')

    def test___setattr__(self):
        self.prototype.attr2 = 'value2'
        self.assertEqual(self.updates, [self.update])
        # Check update_class call
        self.prototype._update_class.assert_called_with(
            '__setattr__', 'attr2', 'value2')

    def test___copy__(self):
        self.prototype.attr2 = 'value2'
        copied_prototype = self.prototype.__copy__('arg2', kwarg2='kwarg2')
        self.assertIsInstance(copied_prototype, self.Prototype)
        self.assertEqual(copied_prototype._class, self.Attribute)
        self.assertEqual(copied_prototype._updates, [self.update])
        self.assertEqual(copied_prototype._args, ('arg1', 'arg2'))
        self.assertEqual(copied_prototype._kwargs,
            {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2'})

    def test___build__(self):
        self.prototype.attr2 = 'value2'
        attribute = self.prototype.__build__('module')
        self.assertIsInstance(attribute, self.Attribute)
        # Check __build__ call
        attribute.__build__.assert_called_with(
            'module', *self.args, **self.kwargs)
        # Check update call
        self.update.apply.assert_called_with(attribute)

    # Protected

    def _make_mock_attribute_class(self):
        class MockAttribute:
            # Public
            __build__ = Mock()
            attr1 = 'value1'
        return MockAttribute

    def _make_mock_prototype_class(self, update):
        class MockPrototype(TaskPrototype):
            # Protected
            _update_class = Mock(return_value=update)
        return MockPrototype
