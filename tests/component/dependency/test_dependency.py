import unittest
from unittest.mock import Mock, patch
from run.dependency.dependency import Dependency


class DependencyTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.successor = Mock()
        self.Dependency = self._make_mock_dependency()
        self.dependency = self.Dependency('task', *self.args, **self.kwargs)
        self.dependency.bind(self.successor)

    def test___repr__(self):
        self.successor.meta_module.task.__repr__ = lambda self: 'task'
        self.assertEqual(repr(self.dependency),
            "MockDependency task('arg1', kwarg1='kwarg1')")

    def test___repr___disabled(self):
        self.successor.meta_module.task.__repr__ = lambda self: 'task'
        self.dependency.disable()
        self.assertEqual(repr(self.dependency),
            "MockDependency task('arg1', kwarg1='kwarg1') [disabled]")

    def test___repr___task_not_existent(self):
        self.successor.meta_module.task = None
        self.assertEqual(repr(self.dependency),
            'MockDependency <NotExistent "task">')

    def test___call__(self):
        method = Mock()
        self.assertEqual(
            self.dependency(method),
            self.dependency._convert.return_value)
        # Check convert call
        self.dependency._convert.assert_called_with(method)
        # Check convert's return_value (prototype) depend call
        prototype = self.dependency._convert.return_value
        prototype.meta_depend.assert_called_with(self.dependency)

    def test_bind(self):
        self.dependency.bind('task')
        self.assertEqual(self.dependency.successor, 'task')

    def test_enable(self):
        self.dependency.enable()
        self.assertTrue(self.dependency.enabled)

    def test_disable(self):
        self.dependency.disable()
        self.assertFalse(self.dependency.enabled)

    def test_invoke(self):
        self.dependency.invoke()
        # Check task call
        self.successor.meta_module.task.assert_called_with(
            *self.args, **self.kwargs)

    def test_invoke_task_not_existent(self):
        self.successor.meta_module = Mock(spec=[])
        self.assertRaises(AttributeError, self.dependency.invoke)

    @patch('logging.getLogger')
    def test_invoke_task_not_existent_and_strict_is_false(self, getLogger):
        self.successor.meta_strict = False
        self.successor.meta_module = Mock(spec=[])
        self.dependency.invoke()
        # Check getLogger call
        self.assertTrue(getLogger.called)
        # Check getLogger's return value (logger) warning call
        self.assertTrue(getLogger.return_value.warning.called)

    def test_invoke_not_bound(self):
        self.dependency.bind(None)
        self.assertRaises(RuntimeError, self.dependency.invoke)

    def test_enabled(self):
        self.assertTrue(self.dependency.enabled)

    def test_predecessor(self):
        self.assertEqual(
            self.dependency.predecessor,
            self.successor.meta_module.task)

    def test_successor(self):
        self.assertEqual(
            self.dependency.successor,
            self.successor)

    # Protected

    def _make_mock_dependency(self):
        class MockDependency(Dependency):
            # Public
            resolve = Mock()
            # Protected
            _convert = Mock()
        return MockDependency
