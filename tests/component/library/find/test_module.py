import unittest
from unittest.mock import Mock, ANY, patch
from importlib import import_module
component = import_module('run.library.find.module')


@unittest.skip
class FindModuleTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.FoundModule = Mock(
            return_value=Mock(meta_tasks={}, __meta_update__=Mock()))
        self.find = Mock(return_value=self.FoundModule)
        patch.object(component, 'find_modules', self.find).start()

    # Tests

    def test(self):
        self.module = component.FindModule(
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
        self.find.assert_called_with(
            target=component.Module,
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
