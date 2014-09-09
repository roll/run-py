import unittest
from unittest.mock import Mock, ANY
from run.library.cluster import ClusterModule, ClusterTask


class ClusterModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.task = Mock()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.FoundModule = Mock(
            return_value=Mock(meta_tasks={'task': self.task}))
        self.Module = self._make_mock_module_class(self.FoundModule)

    def test(self):
        self.module = self.Module(
            meta_module=None,
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively')
        self.assertEqual(self.module.task(), [self.task.return_value])
        # Check find call
        self.Module._find.assert_called_with(
            target=self.Module._Module,
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively',
            filters=ANY)
        # Check FoundModule call
        self.FoundModule.assert_called_with(meta_module=self.module)

    # Protected

    def _make_mock_module_class(self, FoundModule):
        class MockModule(ClusterModule):
            # Protected
            _find = Mock(return_value=[FoundModule])
            _Module = Mock()
        return MockModule


class ClusterTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.nested_task1 = Mock()
        self.nested_task2 = Mock()
        self.task = ClusterTask(
            [self.nested_task1, self.nested_task2], meta_module=None)

    def test___call__(self):
        self.assertEqual(
            self.task(*self.args, **self.kwargs),
            [self.nested_task1.return_value,
             self.nested_task2.return_value])
        # Check nested tasks calls
        self.nested_task1.assert_called_with(*self.args, **self.kwargs)
        self.nested_task2.assert_called_with(*self.args, **self.kwargs)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)