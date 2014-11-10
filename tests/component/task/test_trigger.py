import unittest
from unittest.mock import patch
from importlib import import_module
component = import_module('run.task.trigger')


class trigger_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.invoke = patch.object(component.trigger, 'invoke').start()
        self.trigger = component.trigger('task')

    # Tests

    def test_resolve(self):
        self.trigger.resolve()
        self.assertEqual(self.invoke.call_count, 0)

    def test_resolve_fail_is_false(self):
        self.trigger.resolve(fail=False)
        self.assertEqual(self.invoke.call_count, 1)

    def test_resolve_fail_is_false_and_on_success_is_false(self):
        self.trigger = component.trigger('task', on_success=False)
        self.trigger.resolve(fail=False)
        self.assertEqual(self.invoke.call_count, 0)

    def test_resolve_fail_is_true(self):
        self.trigger.resolve(fail=True)
        self.assertEqual(self.invoke.call_count, 0)

    def test_resolve_fail_is_true_and_on_fail_is_true(self):
        self.trigger = component.trigger('task', on_fail=True)
        self.trigger.resolve(fail=True)
        self.assertEqual(self.invoke.call_count, 1)
