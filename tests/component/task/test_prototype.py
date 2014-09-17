import unittest
from unittest.mock import Mock, patch
from run.task import prototype


class PrototypeTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.update = Mock()
        self.TaskUpdate = Mock(return_value=self.update)
        patch.object(prototype, 'TaskUpdate', self.TaskUpdate).start()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.Task = self._make_mock_task_class()
        self.prototype = prototype.Prototype(
            *self.args, meta_class=self.Task, **self.kwargs)

    def test___getattr__(self):
        self.assertEqual(self.prototype.attr2, Mock)

    def test___setattr__(self):
        self.prototype.attr3.nested_attr3 = 'value2'
        # Check update_class call
        self.TaskUpdate.assert_called_with(
            '__setattr__', 'attr3.nested_attr3', 'value2')

    def test___call__(self):
        self.prototype.attr3.nested_attr3(*self.args, **self.kwargs)
        # Check update_class call
        self.TaskUpdate.assert_called_with(
            'attr3.nested_attr3', *self.args, **self.kwargs)

    def test___call___before_getattr(self):
        self.assertRaises(TypeError, self.prototype)

    def test___meta_fork__(self):
        self.prototype.attr2 = 'value2'
        fork = self.prototype.__meta_fork__('arg2', kwarg2='kwarg2')
        self.assertIsInstance(fork, prototype.Prototype)

    # TODO: implement
    def test___meta_build__(self):
        pass

    # Protected

    def _make_mock_task_class(self):
        class MockTask:
            # Public
            __meta_create__ = Mock()
            __meta_update__ = Mock()
            attr1 = 'value1'
            attr2 = Mock
        return MockTask
