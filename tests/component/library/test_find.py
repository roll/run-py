import unittest
from functools import partial
from unittest.mock import Mock, patch, ANY
from run.library import find


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
        class MockModule(find.FindModule):
            # Protected
            _find = Mock(return_value=FoundModule)
            _Module = Mock()
        return MockModule


class FindTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.ptask = partial(find.FindTask, meta_module=None)

    @patch.object(find.find, 'find_strings')
    def test___call__(self, find_string):
        task = self.ptask()
        result = task(*self.args, **self.kwargs)
        self.assertEqual(result, find_string.return_value)
        find_string.assert_called_with(*self.args, **self.kwargs)

    def test___call___with_unsopported_mode(self):
        self.assertRaises(ValueError, self.ptask, mode='unsupported')


class FindVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(find.FindVar, find.Var))
        self.assertTrue(issubclass(find.FindVar, find.FindTask))
