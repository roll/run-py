import unittest
from unittest.mock import Mock
from run.task.prototype import TaskPrototype


# TODO: implement fully
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
        self.prototype.attr2.nested_attr2 = 'value2'
        self.assertEqual(self.updates, [self.update])
        # Check update_class call
        self.prototype._meta_TaskUpdate.assert_called_with(
            '__setattr__', 'attr2.nested_attr2', 'value2')

    def test___call__(self):
        self.prototype.attr2.nested_attr2(*self.args, **self.kwargs)
        self.assertEqual(self.updates, [self.update])
        # Check update_class call
        self.prototype._meta_TaskUpdate.assert_called_with(
            'attr2.nested_attr2', *self.args, **self.kwargs)

    def test___call___before_getattr(self):
        self.assertRaises(TypeError, self.prototype)

    def test___meta_fork__(self):
        self.prototype.attr2 = 'value2'
        fork = self.prototype.__meta_fork__('arg2', kwarg2='kwarg2')
        self.assertIsInstance(fork, self.Prototype)
        self.assertEqual(fork._meta_class, self.Task)
        self.assertEqual(fork._meta_updates, [self.update])
        self.assertEqual(fork._meta_args, ('arg1', 'arg2'))
        self.assertEqual(fork._meta_kwargs,
            {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2'})

    # Protected

    def _make_mock_task_class(self):
        class MockTask:
            # Public
            __meta_create__ = Mock()
            __meta_update__ = Mock()
            attr1 = 'value1'
        return MockTask

    def _make_mock_prototype_class(self, update):
        class MockPrototype(TaskPrototype):
            # Protected
            _meta_TaskUpdate = Mock(return_value=update)
        return MockPrototype
