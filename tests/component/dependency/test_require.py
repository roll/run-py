import unittest
from unittest.mock import Mock
from run.dependency.require import require

class require_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.require = require('task')
        self.require.invoke = Mock()

    def test_resolve(self):
        self.require.resolve()
        self.require.resolve()
        # Check invoke call
        self.assertEqual(self.require.invoke.call_count, 1)

    def test_resolve_not_enabled(self):
        self.require.disable()
        self.require.resolve()
        # Check invoke call
        self.assertEqual(self.require.invoke.call_count, 0)

    def test_resolve_failed(self):
        self.require.resolve(failed=True)
        # Check invoke call
        self.assertEqual(self.require.invoke.call_count, 0)
