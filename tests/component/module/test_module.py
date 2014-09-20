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
        self.print = Mock()
        self.pprint = Mock()
        patch.object(component, 'print', self.print).start()
        patch.object(component, 'pprint', self.pprint).start()
        self.Module = self.make_mock_module_class()
        self.module = self.Module(meta_module=None)
        self.ParentModule = self.make_mock_parent_module_class()
        self.parent_module = self.ParentModule()

    # Helpers

    def make_mock_module_class(self):
        class MockModule(component.Module):
            """docstring"""
            # Public
            meta_plain = True
            def task(self):
                pass
        return MockModule

    def make_mock_parent_module_class(self):
        class MockParentModule:
            # Public
            meta_cache = 'cache'
            meta_dispatcher = Mock(add_signal=Mock())
            meta_fallback = 'fallback'
            meta_fullname = '[key]'
            meta_is_main_module = True
            meta_name = ''
            meta_qualname = ''
            meta_strict = 'strict'
            meta_tasks = {}
            meta_workdir = None
            @property
            def meta_main_module(self):
                return self
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

    def test_meta_lookup(self):
        self.assertEqual(
            self.module.meta_lookup('task'), self.module.task)

    def test_meta_lookup_nested(self):
        self.Module.meta_tasks = {
            'module': self.module, 'task': self.module.task}
        self.assertEqual(
            self.module.meta_lookup('module.task'), self.module.task)

    def test_meta_invoke(self):
        self.Module.meta_default = 'default'
        self.Module.default = Mock()
        self.assertEqual(
            self.module.meta_invoke(*self.args, **self.kwargs),
            self.module.default.return_value)
        self.assertIsInstance(self.module, self.Module)
        # Check default call
        self.module.default.assert_called_with(*self.args, **self.kwargs)

    def test_meta_workdir(self):
        self.assertRegex(self.module.meta_workdir,
                         r'.*tests.component.module')

    def test_meta_workdir_with_parent_module(self):
        self.Module.meta_inherit = ['meta_workdir']
        self.module = self.Module(meta_module=self.parent_module)
        self.assertEqual(
            self.module.meta_workdir,
            self.module.meta_module.meta_workdir)

    @unittest.skip
    def test_meta_workdir_setter(self):
        self.Module.meta_workdir = 'workdir'
        self.assertEqual(self.module.meta_workdir, 'workdir')

    def test_meta_fullname(self):
        self.assertEqual(self.module.meta_fullname, '')

    def test_meta_fullname_with_meta_key(self):
        self.Module.meta_key = 'key'
        self.assertEqual(self.module.meta_fullname, '[key]')

    def test_meta_is_main_module(self):
        self.assertTrue(self.module.meta_is_main_module)

    def test_meta_is_main_module_with_parent_module(self):
        self.module = self.Module(meta_module=self.parent_module)
        self.assertFalse(self.module.meta_is_main_module)

    def test_meta_main_module(self):
        self.assertIs(self.module.meta_main_module, self.module)

    def test_meta_main_module_with_parent_module(self):
        self.module = self.Module(meta_module=self.parent_module)
        self.assertIs(self.module.meta_main_module, self.parent_module)

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
            meta_module=self.parent_module,
            meta_fallback=None)
        self.parent_module.meta_tasks = {'module': self.module}
        self.module.list()
        # Check print call
        self.print.assert_called_once_with(
            '[key] module.info\n'
            '[key] module.list\n'
            '[key] module.meta\n'
            '[key] module.task')

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
            'Type: FunctionTask\n'
            'Dependencies: []\n'
            'Default arguments: ()\n'
            'Default keyword arguments: {}\n'
            '---\n'
            'Print information.')

    def test_meta(self):
        self.module.meta()
        # Check pprint call
        argument = self.pprint.call_args[0][0]
        self.assertEqual(len(argument), 28)

    def test_meta_with_task(self):
        self.module.meta('meta')
        # Check pprint call
        argument = self.pprint.call_args[0][0]
        self.assertEqual(len(argument), 22)
