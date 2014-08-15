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
        self.Task = self._make_mock_task_class()
        self.Prototype = self._make_mock_prototype_class(self.update)
        self.prototype = self.Prototype(
            *self.args,
            meta_class=self.Task,
            meta_updates=self.updates,
            **self.kwargs)

    def test___setattr__(self):
        self.prototype.attr2 = 'value2'
        self.assertEqual(self.updates, [self.update])
        # Check update_class call
        self.prototype._meta_TaskUpdate.assert_called_with(
            '__setattr__', 'attr2', 'value2')

    def __meta_fork__(self):
        self.prototype.attr2 = 'value2'
        fork = self.prototype.__meta_fork__('arg2', kwarg2='kwarg2')
        self.assertIsInstance(fork, self.Prototype)
        self.assertEqual(fork._class, self.Task)
        self.assertEqual(fork._updates, [self.update])
        self.assertEqual(fork._args, ('arg1', 'arg2'))
        self.assertEqual(fork._kwargs,
            {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2'})

    @unittest.skip('not fixed after refactoring')
    def test___meta_init__(self):
        self.prototype.attr2 = 'value2'
        task = self.prototype.__meta_init__('module')
        self.assertIsInstance(task, self.Task)
        # Check __meta_init__ call
        task.__meta_init__.assert_called_with(
            *self.args,
            meta_module='module',
            meta_updates=self.updates,
            **self.kwargs)

    # Protected

    def _make_mock_task_class(self):
        class MockTask:
            # Public
            __meta_create__ = Mock()
            __meta_init__ = Mock()
            __meta_update__ = Mock()
            attr1 = 'value1'
        return MockTask

    def _make_mock_prototype_class(self, update):
        class MockPrototype(TaskPrototype):
            # Protected
            _meta_TaskUpdate = Mock(return_value=update)
        return MockPrototype
