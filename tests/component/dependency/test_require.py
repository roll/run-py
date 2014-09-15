import unittest
from unittest.mock import patch
from run.dependency.require import require


class require_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.invoke = patch.object(require, 'invoke').start()
        self.require = require('task')

    def test_resolve(self):
        self.require.resolve()
        self.require.resolve()
        self.assertEqual(self.invoke.call_count, 1)

    def test_resolve_not_enabled(self):
        self.require.disable()
        self.require.resolve()
        self.assertEqual(self.invoke.call_count, 0)

    def test_resolve_failed_not_none(self):
        self.require.resolve(failed='failed')
        self.assertEqual(self.invoke.call_count, 0)
