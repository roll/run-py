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
        self.module = self.Module(Build=True)
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
            Basedir = '/basedir'
            Cache = 'cache'
            Chdir = 'chdir'
            Fallback = 'fallback'
            Name = ''
            Qualname = 'MAIN'
            Tasks = {}
            @property
            def Main(self):
                return self
            def Locate(self, *args, **kwargs):
                return self.Basedir
            def Notify(self, event):
                pass
        return MockParentModule

    # Tests

    def test___call__(self):
        self.Module.Default = 'default'
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

    def test_Invoke(self):
        self.Module.Default = 'default'
        self.Module.default = Mock()
        self.assertEqual(
            self.module.Invoke(*self.args, **self.kwargs),
            self.module.default.return_value)
        self.assertIsInstance(self.module, self.Module)
        # Check default call
        self.module.default.assert_called_with(*self.args, **self.kwargs)

    def test_Basedir(self):
        self.assertRegex(self.module.Basedir,
                         r'.*tests.component.module')

    def test_Locate_with_parent_module_and_Basedir_is_none(self):
        self.module = self.Module(
            Build=True,
            Basedir=None,
            Module=self.parent_module)
        self.assertEqual(self.module.Locate(), '/basedir')

    def test_Main(self):
        self.assertIs(self.module.Main, self.module)

    @unittest.skip
    def test_Main_with_parent_module(self):
        self.module = self.Module(
            Build=True,
            Module=self.parent_module)
        self.assertIs(self.module.Main, self.parent_module)

    def test_Tasks(self):
        self.assertEqual(sorted(self.module.Tasks),
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
            Build=True,
            Module=self.parent_module,
            Chdir=False,
            Fallback=None)
        self.parent_module.Tasks = {'module': self.module}
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
            'Print task information.')

    def test_meta(self):
        self.module.meta()
        # Check pprint call
        argument = self.pprint.call_args[0][0]
        self.assertEqual(len(argument), 20)

    def test_meta_with_task(self):
        self.module.meta('meta')
        # Check pprint call
        argument = self.pprint.call_args[0][0]
        self.assertEqual(len(argument), 16)
