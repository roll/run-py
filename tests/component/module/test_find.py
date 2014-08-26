import unittest
from unittest.mock import Mock, ANY
from run.module.find import FindModule


class FindModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.FoundModule = Mock(
            return_value=Mock(meta_tasks={}, __meta_update__=Mock()))
        self.Module = self._make_mock_module_class(self.FoundModule)

    def test(self):
        self.module = self.Module(
            *self.args,
            meta_module=None,
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively',
            **self.kwargs)
        self.assertEqual(self.module, self.FoundModule.return_value)
        # Check find call
        self.Module._find.assert_called_with(
            target=self.Module._Module,
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively',
            filters=ANY,
            getfirst=True)
        # Check FoundModule call
        self.FoundModule.assert_called_with(
            *self.args,
            meta_module=ANY,
            meta_updates=[],
            **self.kwargs)

    # Protected

    def _make_mock_module_class(self, FoundModule):
        class MockModule(FindModule):
            # Protected
            _find = Mock(return_value=FoundModule)
            _Module = Mock()
        return MockModule
