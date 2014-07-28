import os
import unittest
from unittest.mock import patch
from run.module.null import NullModule

class NullModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.module = NullModule()

    def test___bool__(self):
        self.assertFalse(self.module)

    def test___repr__(self):
        self.assertTrue(repr(self.module))

    def test_meta_tasks(self):
        self.assertEqual(self.module.meta_tasks, {})

    def test_meta_basedir(self):
        self.assertEqual(self.module.meta_basedir, os.getcwd())

    @patch.object(NullModule, '_default_meta_cache')
    def test_meta_cache(self, cache):
        self.assertEqual(self.module.meta_cache, cache)

    @patch.object(NullModule, '_default_meta_chdir')
    def test_meta_chdir(self, chdir):
        self.assertEqual(self.module.meta_chdir, chdir)

    @patch.object(NullModule, '_dispatcher_class')
    def test_meta_dispatcher(self, dispatcher_class):
        self.assertEqual(self.module.meta_dispatcher,
                         dispatcher_class.return_value)

    def test_meta_docstring(self):
        self.assertEqual(self.module.meta_docstring, 'NullModule')

    @patch.object(NullModule, '_default_meta_fallback')
    def test_meta_fallback(self, fallback):
        self.assertEqual(self.module.meta_fallback, fallback)

    def test_meta_is_main_module(self):
        self.assertEqual(self.module.meta_is_main_module, True)

    def test_meta_main_module(self):
        self.assertEqual(self.module.meta_main_module, self.module)

    def test_meta_module(self):
        self.assertEqual(self.module.meta_module, self.module)

    @patch.object(NullModule, '_default_meta_main_module_name')
    def test_meta_name(self, name):
        self.assertEqual(self.module.meta_name, name)

    def test_meta_qualname(self):
        self.assertEqual(self.module.meta_qualname, '__main__')

    @patch.object(NullModule, '_default_meta_strict')
    def test_meta_strict(self, strict):
        self.assertEqual(self.module.meta_strict, strict)

    def test_meta_tags(self):
        self.assertEqual(self.module.meta_tags, [])

    def test_meta_type(self):
        self.assertEqual(self.module.meta_type, 'NullModule')
