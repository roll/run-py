import unittest
from unittest.mock import Mock, ANY
from run.module.cluster import ClusterModule

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
