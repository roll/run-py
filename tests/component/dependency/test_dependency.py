import unittest
from unittest.mock import MagicMock, Mock, patch
from run.dependency.dependency import Dependency

class DependencyTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.attribute = Mock()
        self.Dependency = self._make_mock_dependency()
        self.dependency = self.Dependency('task', *self.args, **self.kwargs)
        self.dependency.bind(self.attribute)

    def test___repr__(self):
        self.assertEqual(repr(self.dependency),
            "MockDependency task('arg1', kwarg1='kwarg1')")

    def test___repr___task_not_existent(self):
        self.dependency._getattribute.return_value = None
        self.assertEqual(repr(self.dependency),
            'MockDependency <NotExistent "task">')

    def test___call__(self):
        method = Mock()
        self.assertEqual(
            self.dependency(method),
            self.dependency._method_task_class.return_value)
        # Check MethodTask call
        self.dependency._method_task_class.assert_called_with(method)
        # Check MethodTask's return_value (prototype) depend call
        prototype = self.dependency._method_task_class.return_value
        prototype.depend.assert_called_with(self.dependency)

    def test___call___method_is_prototype(self):
        prototype = MagicMock()
        self.assertEqual(self.dependency(prototype), prototype)
        # Check prototype call
        prototype.depend.assert_called_with(self.dependency)

    def test_bind(self):
        self.dependency.bind('attribute')
        self.assertEqual(self.dependency.attribute, 'attribute')

    def test_enable(self):
        self.dependency.enable()
        self.assertTrue(self.dependency.enabled)

    def test_disable(self):
        self.dependency.disable()
        self.assertFalse(self.dependency.enabled)

    def test_invoke(self):
        self.dependency.invoke()
        # Check getattribute call
        self.dependency._getattribute.assert_called_with(
            self.attribute.meta_module, 'task',
            category=self.dependency._task_class, getvalue=True)
        # Check getattribute return value (task) call
        self.dependency._getattribute.return_value.assert_called_with(
            *self.args, **self.kwargs)

    def test_invoke_task_not_existent(self):
        self.dependency._getattribute.side_effect = AttributeError()
        self.assertRaises(AttributeError, self.dependency.invoke)

    @patch('logging.getLogger')
    def test_invoke_task_not_existent_and_strict_is_false(self, getLogger):
        self.attribute.meta_strict = False
        self.dependency._getattribute.side_effect = AttributeError()
        self.dependency.invoke()
        # Check getLogger call
        self.assertTrue(getLogger.called)
        # Check getLogger's return value (logger) warning call
        self.assertTrue(getLogger.return_value.warning.called)
        # Check getattribute's return value (task) NO call
        self.assertFalse(self.dependency._getattribute.return_value.called)

    def test_invoke_not_bound(self):
        self.dependency.bind(None)
        self.assertRaises(RuntimeError, self.dependency.invoke)

    def test_attribute(self):
        self.assertEqual(self.dependency.attribute, self.attribute)

    def test_enabled(self):
        self.assertTrue(self.dependency.enabled)

    def test_task(self):
        self.assertEqual(self.dependency.task, 'task')

    # Protected

    def _make_mock_dependency(self):
        class MockDependency(Dependency):
            # Public
            resolve = Mock()
            # Protected
            _attribute_prototype_class = MagicMock
            _getattribute = Mock(return_value=
                Mock(__repr__=lambda self: 'task'))
            _method_task_class = Mock()
            _task_class = Mock()
        return MockDependency
