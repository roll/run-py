import unittest
from importlib import import_module
from unittest.mock import Mock, patch
component = import_module('run.module.module')


class ModuleTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.print = patch.object(component, 'print').start()
        self.pprint = patch.object(component, 'pprint').start()
        patch.object(component.settings, 'plain', True).start()
        self.Module = self.make_mock_module_class()
        self.module = self.Module(meta_build=True)
        self.ParentModule = self.make_mock_parent_module_class()
        self.parent_module = self.ParentModule()

    # Helpers

    def make_mock_module_class(self):
        class MockModule(component.Module):
            """docstring"""
            # Public
            def task(self):
                pass
        return MockModule

    def make_mock_parent_module_class(self):
        class MockParentModule:
            # Public
            meta_basedir = '/basedir'
            meta_cache = 'cache'
            meta_chdir = 'chdir'
            meta_fallback = 'fallback'
            meta_name = ''
            meta_qualname = 'MAIN'
            meta_tasks = {}
            @property
            def meta_root(self):
                return self
            def meta_path(self, *args, **kwargs):
                return self.meta_basedir
            def meta_notify(self, event):
                pass
        return MockParentModule

    # Tests

    def test___call__(self):
        self.Module.meta_default = 'default'
        self.Module.default = Mock()
        self.assertEqual(
            self.module(*self.args, **self.kwargs),
            self.module.default.return_value)
        self.assertIsInstance(self.module, self.Module)
        # Check default call
        self.module.default.assert_called_with(*self.args, **self.kwargs)

    def test___getattribute__(self):
        self.assertEqual(getattr(self.module, 'task'), self.module.task)

    def test___getattribute___nested(self):
        self.Module.module = self.module
        self.assertEqual(
            getattr(self.module, 'module.task'), self.module.task)

    def test___getattribute___not_existent(self):
        self.assertRaises(AttributeError,
            getattr, self.module, 'not_existent')

    def test_meta_invoke(self):
        self.Module.meta_default = 'default'
        self.Module.default = Mock()
        self.assertEqual(
            self.module.meta_invoke(*self.args, **self.kwargs),
            self.module.default.return_value)
        self.assertIsInstance(self.module, self.Module)
        # Check default call
        self.module.default.assert_called_with(*self.args, **self.kwargs)

    def test_meta_basedir(self):
        self.assertRegex(self.module.meta_basedir,
                         r'.*tests.component.module')

    def test_meta_root(self):
        self.assertIs(self.module.meta_root, self.module)

    @unittest.skip
    def test_meta_root_with_parent_module(self):
        self.module = self.Module(
            meta_build=True,
            meta_module=self.parent_module)
        self.assertIs(self.module.meta_root, self.parent_module)

    def test_meta_path_with_parent_module_and_meta_basedir_is_none(self):
        self.module = self.Module(
            meta_build=True,
            meta_basedir=None,
            meta_module=self.parent_module)
        self.assertEqual(self.module.meta_path(), '/basedir')

    def test_meta_tags(self):
        self.assertEqual(self.module.meta_tags, [])

    def test_meta_tasks(self):
        self.assertEqual(sorted(self.module.meta_tasks),
            ['info', 'list', 'meta', 'task'])

    def test_list(self):
        self.module.list()
        # Check print call
        self.print.assert_called_once_with(
            'info\n'
            'list\n'
            'meta\n'
            'task')

    def test_list_with_parent_module(self):
        # We have to recreate class for builtin tasks
        self.Module = self.make_mock_module_class()
        self.module = self.Module(
            meta_build=True,
            meta_module=self.parent_module,
            meta_chdir=False,
            meta_fallback=None)
        self.parent_module.meta_tasks = {'module': self.module}
        self.module.list()
        # Check print call
        self.print.assert_called_once_with(
            'MAIN.module.info\n'
            'MAIN.module.list\n'
            'MAIN.module.meta\n'
            'MAIN.module.task')

    def test_info(self):
        self.module.info()
        # Check print call
        self.print.assert_called_once_with(
            '(*args, **kwargs)\n'
            '---\n'
            'Type: MockModule\nDependencies: []\n'
            'Default arguments: ()\n'
            'Default keyword arguments: {}\n'
            '---\n'
            'docstring')

    def test_info_with_task(self):
        self.module.info('info')
        # Check print call
        self.print.assert_called_once_with(
            'info(task=None)\n'
            '---\n'
            'Type: MethodTask\n'
            'Dependencies: []\n'
            'Default arguments: ()\n'
            'Default keyword arguments: {}\n'
            '---\n'
            'Print information.')

    def test_meta(self):
        self.module.meta()
        # Check pprint call
        argument = self.pprint.call_args[0][0]
        self.assertEqual(len(argument), 21)

    def test_meta_with_task(self):
        self.module.meta('meta')
        # Check pprint call
        argument = self.pprint.call_args[0][0]
        self.assertEqual(len(argument), 15)
