import unittest
from unittest.mock import patch
from importlib import import_module
component = import_module('run.dependency.require')


class require_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.invoke = patch.object(component.require, 'invoke').start()
        self.require = component.require('task')

    # Tests

    def test_resolve(self):
        self.require.resolve()
        self.require.resolve()
        self.assertEqual(self.invoke.call_count, 1)

    def test_resolve_failed_is_not_none(self):
        self.require.resolve(failed='failed')
        self.assertEqual(self.invoke.call_count, 0)
