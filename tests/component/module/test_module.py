import unittest
from unittest.mock import Mock, call
from run.module.module import Module

class ModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.ParentModule = self._make_mock_parent_module_class()
        self.parent_module = self.ParentModule()
        self.Module = self._make_mock_module_class()
        self.module = self.Module(meta_module=None)

    def test(self):
        self.assertIsInstance(self.module, self.Module)

    def test___get__(self):
        self.assertIs(self.module.__get__(None), self.module)

    def test___set__(self):
        self.assertRaises(AttributeError, self.module.__set__, None, 'value')

    def test___getattr___no_attribute(self):
        self.assertRaises(AttributeError, getattr, self.module, 'no_attr')
        self.assertRaises(AttributeError, getattr, self.module, 'no_attr.req')

    def test___call__(self):
        args = ('arg1',)
        kwargs = {'kwarg1': 'kwarg1'}
        self.Module.default = Mock()
        self.assertEqual(
            self.module(*args, **kwargs),
            self.module.default.return_value)
        # Check default call
        self.module.default.assert_called_with(*args, **kwargs)

    def test_meta_attributes(self):
        self.assertEqual(sorted(self.module.meta_attributes),
            ['attr1', 'default', 'info', 'list', 'meta'])

    def test_meta_basedir(self):
        self.assertRegex(self.module.meta_basedir,
                         r'.*tests.component.module')

    def test_meta_basedir_setter(self):
        self.module.meta_basedir = 'basedir'
        self.assertEqual(self.module.meta_basedir, 'basedir')

    def test_meta_basedir_with_parent_module(self):
        self.module = self.Module(meta_module=self.parent_module)
        self.assertEqual(self.module.meta_basedir, 'basedir')

    def test_meta_dispatcher(self):
        self.assertEqual(self.module.meta_dispatcher,
                         self.module.meta_module.meta_dispatcher)

    def test_meta_docstring(self):
        self.assertEqual(self.module.meta_docstring, 'docstring')

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

    def test_meta_module(self):
        # NullModule
        self.assertNotEqual(self.module.meta_module, None)
        self.assertFalse(self.module.meta_module)

    def test_meta_name(self):
        self.assertEqual(self.module.meta_name, '__main__')

    def test_meta_name_with_parent_module(self):
        self.module = self.Module(meta_module=self.parent_module)
        self.parent_module.meta_attributes = {'module': self.module}
        self.assertEqual(self.module.meta_name, 'module')

    def test_meta_qualname(self):
        self.assertEqual(self.module.meta_qualname, '__main__')

    def test_meta_qualname_with_parent_module(self):
        self.module = self.Module(meta_module=self.parent_module)
        self.parent_module.meta_attributes = {'module': self.module}
        self.assertEqual(self.module.meta_qualname, '[parent_module] module')

    def test_meta_tags(self):
        self.assertEqual(self.module.meta_tags, [])

    def test_meta_type(self):
        self.assertEqual(self.module.meta_type, 'MockModule')

    def test_list(self):
        self.module.list()
        # Check print call
        self.module._print.assert_has_calls([
            call('attr1'),
            call('default'),
            call('info'),
            call('list'),
            call('meta')])

    def test_list_with_parent_module(self):
        # We have to recreate class for builtin tasks
        self.Module = self._make_mock_module_class()
        self.module = self.Module(
            meta_module=self.parent_module,
            meta_chdir=False,
            meta_fallback=None)
        self.parent_module.meta_attributes = {'module': self.module}
        self.module.list()
        # Check print call
        self.module._print.assert_has_calls([
            call('[parent_module] module.attr1'),
            call('[parent_module] module.default'),
            call('[parent_module] module.info'),
            call('[parent_module] module.list'),
            call('[parent_module] module.meta')])

    def test_info(self):
        self.module.info()
        # Check print call
        self.assertTrue(self.module._print.called)

    def test_meta(self):
        self.module.meta()
        # Check print call
        self.assertTrue(self.module._pprint.called)

    # Protected

    def _make_mock_parent_module_class(self):
        class MockParentModule:
            # Public
            meta_attributes = {}
            meta_basedir = 'basedir'
            meta_cache = 'cache'
            meta_chdir = 'chdir'
            meta_fallback = 'fallback'
            meta_dispatcher = Mock(add_signal=Mock())
            meta_is_main_module = True
            meta_name = 'parent_module'
            meta_qualname = 'parent_module'
            meta_strict = 'strict'
            @property
            def meta_main_module(self):
                return self
        return MockParentModule

    def _make_mock_module_class(self):
        class MockModule(Module):
            """docstring"""
            # Public
            attr1 = 'value1'
            # Protected
            _default_meta_main_module_name = '__main__'
            _print = Mock()
            _pprint = Mock()
        return MockModule
