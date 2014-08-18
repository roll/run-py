import os
import unittest
from unittest.mock import patch
from run.task.null_module import NullModule


class NullModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.module = NullModule()

    def test___bool__(self):
        self.assertFalse(self.module)

    def test___repr__(self):
        self.assertTrue(repr(self.module))

    def test_meta_lookup(self):
        self.assertRaises(KeyError, self.module.meta_lookup, 'name')

    def test_meta_basedir(self):
        self.assertEqual(self.module.meta_basedir, os.getcwd())

    @patch.object(NullModule, '_meta_default_cache')
    def test_meta_cache(self, cache):
        self.assertEqual(self.module.meta_cache, cache)

    @patch.object(NullModule, '_meta_default_chdir')
    def test_meta_chdir(self, chdir):
        self.assertEqual(self.module.meta_chdir, chdir)

    @patch.object(NullModule, '_meta_NullDispatcher')
    def test_meta_dispatcher(self, NullDispatcher):
        self.assertEqual(self.module.meta_dispatcher,
                         NullDispatcher.return_value)

    @patch.object(NullModule, '_meta_default_fallback')
    def test_meta_fallback(self, fallback):
        self.assertEqual(self.module.meta_fallback, fallback)

    def test_meta_fullname(self):
        self.assertEqual(self.module.meta_fullname, '')

    def test_meta_is_main_module(self):
        self.assertEqual(self.module.meta_is_main_module, True)

    def test_meta_qualname(self):
        self.assertEqual(self.module.meta_qualname, '')

    def test_meta_main_module(self):
        self.assertEqual(self.module.meta_main_module, self.module)

    @patch.object(NullModule, '_meta_default_plain')
    def test_meta_plain(self, plain):
        self.assertEqual(self.module.meta_plain, plain)

    @patch.object(NullModule, '_meta_default_strict')
    def test_meta_strict(self, strict):
        self.assertEqual(self.module.meta_strict, strict)

    def test_meta_tasks(self):
        self.assertEqual(self.module.meta_tasks, {})
