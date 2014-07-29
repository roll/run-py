import unittest
from unittest.mock import Mock, call
from run.module.module import Module

class ModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Module = self._make_mock_module_class()
        self.module = self.Module(meta_module=None)
        self.ParentModule = self._make_mock_parent_module_class()
        self.parent_module = self.ParentModule()

    def test___call__(self):
        args = ('arg1',)
        kwargs = {'kwarg1': 'kwarg1'}
        self.Module.default = Mock()
        self.assertEqual(
            self.module(*args, **kwargs),
            self.module.default.return_value)
        self.assertIsInstance(self.module, self.Module)
        # Check default call
        self.module.default.assert_called_with(*args, **kwargs)

    def test___getattribute___not_existent(self):
        self.assertRaises(AttributeError,
            self.module.__getattribute__, 'not_existent')

    def test___getattribute___nested(self):
        self.Module.module1 = self.module
        result = self.module.__getattribute__('module1.task')
        self.assertEqual(result, self.module.task)

    def test_meta_basedir(self):
        self.assertRegex(self.module.meta_basedir,
                         r'.*tests.component.module')

    def test_meta_basedir_with_parent_module(self):
        self.module = self.Module(meta_module=self.parent_module)
        self.assertEqual(self.module.meta_basedir, 'basedir')

    def test_meta_basedir_setter(self):
        self.module.meta_basedir = 'basedir'
        self.assertEqual(self.module.meta_basedir, 'basedir')

    def test_meta_cache(self):
        self.assertEqual(self.module.meta_cache,
                         self.module.meta_module.meta_cache)

    def test_meta_cache_setter(self):
        self.module.meta_cache = 'cache'
        self.assertEqual(self.module.meta_cache, 'cache')

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

    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, '__main__')

    def test_meta_name_with_parent_module(self):
        self.module = self.Module(meta_module=self.parent_module)
        self.parent_module.meta_tasks = {'module': self.module}
        self.assertEqual(self.module.meta_name, 'module')

    def test_meta_tags(self):
        self.assertEqual(self.module.meta_tags, [])

    def test_meta_tasks(self):
        self.assertEqual(sorted(self.module.meta_tasks),
            ['default', 'info', 'list', 'meta', 'task'])

    def test_list(self):
        self.module.list()
        # Check print call
        self.module._print.assert_has_calls([
            call('default'),
            call('info'),
            call('list'),
            call('meta'),
            call('task')])

    def test_list_with_parent_module(self):
        # We have to recreate class for builtin tasks
        self.Module = self._make_mock_module_class()
        self.module = self.Module(
            meta_module=self.parent_module,
            meta_chdir=False,
            meta_fallback=None)
        self.parent_module.meta_tasks = {'module': self.module}
        self.module.list()
        # Check print call
        self.module._print.assert_has_calls([
            call('[parent_module] module.default'),
            call('[parent_module] module.info'),
            call('[parent_module] module.list'),
            call('[parent_module] module.meta'),
            call('[parent_module] module.task')])

    @unittest.skip('Breaks system tests. Why??')
    def test_list_with_task_is_not_module(self):
        self.assertRaises(TypeError, self.module.list, 'list')

    def test_info(self):
        self.module.info()
        # Check print call
        self.module._print.assert_called_once_with(
            '__main__(*args, **kwargs)\n'
            '---\n'
            'Type: MockModule\nDependencies: []\n'
            'Default arguments: ()\n'
            'Default keyword arguments: {}\n'
            '---\n'
            'docstring')

    def test_info_with_task(self):
        self.module.info('info')
        # Check print call
        self.module._print.assert_called_once_with(
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
        # Check print call
        self.assertTrue(self.module._pprint.called)

    def test_meta_with_task(self):
        self.module.meta('meta')
        # Check print call
        self.assertTrue(self.module._pprint.called)

    # Protected

    def _make_mock_module_class(self):
        class MockModule(Module):
            """docstring"""
            # Public
            def task(self):
                pass
            # Protected
            _default_meta_main_module_name = '__main__'
            _print = Mock()
            _pprint = Mock()
        return MockModule

    def _make_mock_parent_module_class(self):
        class MockParentModule:
            # Public
            meta_basedir = 'basedir'
            meta_cache = 'cache'
            meta_chdir = 'chdir'
            meta_fallback = 'fallback'
            meta_dispatcher = Mock(add_signal=Mock())
            meta_is_main_module = True
            meta_name = 'parent_module'
            meta_qualname = 'parent_module'
            meta_strict = 'strict'
            meta_tasks = {}
            @property
            def meta_main_module(self):
                return self
        return MockParentModule
