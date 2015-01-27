import unittest
from unittest.mock import Mock, patch
from importlib import import_module
component = import_module('run.task.dependency')


class DependencyTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.convert = Mock()
        patch.object(component, 'convert', self.convert).start()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.successor = Mock()
        self.Dependency = self.make_mock_dependency()
        self.dependency = self.Dependency('task', *self.args, **self.kwargs)
        self.dependency.bind(self.successor)

    # Helpers

    def make_mock_dependency(self):
        class MockDependency(component.Dependency):
            # Public
            resolve = Mock()
        return MockDependency

    # Tests

    def test___repr__(self):
        self.successor.Module.task.__repr__ = lambda self: 'task'
        self.assertEqual(repr(self.dependency),
            "MockDependency task('arg1', kwarg1='kwarg1')")

    def test___repr___task_not_existent(self):
        self.successor.Module.task = None
        self.assertEqual(repr(self.dependency),
            'MockDependency <NotExistent "task">')

    def test___call__(self):
        method = Mock()
        self.assertEqual(
            self.dependency(method),
            self.convert.return_value)
        # Check convert call
        self.convert.assert_called_with(method)
        # Check convert's return_value (prototype) depend call
        prototype = self.convert.return_value
        prototype.Depend.assert_called_with(self.dependency)

    def test_bind(self):
        self.dependency.bind('task')
        self.assertEqual(self.dependency.successor, 'task')

    def test_invoke(self):
        self.dependency.invoke()
        # Check task call
        self.successor.Module.task.assert_called_with(
            *self.args, **self.kwargs)

    def test_invoke_task_not_existent(self):
        self.successor.Module = Mock(spec=[])
        self.assertRaises(AttributeError, self.dependency.invoke)

    def test_invoke_not_bound(self):
        self.dependency.bind(None)
        self.assertRaises(RuntimeError, self.dependency.invoke)

    def test_predecessor(self):
        self.assertEqual(
            self.dependency.predecessor,
            self.successor.Module.task)

    def test_successor(self):
        self.assertEqual(
            self.dependency.successor,
            self.successor)
