import unittest
from unittest.mock import patch
from run.dependency.trigger import trigger


class trigger_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.invoke = patch.object(trigger, 'invoke').start()
        self.trigger = trigger('task')

    def test_resolve(self):
        self.trigger.resolve()
        self.assertEqual(self.invoke.call_count, 0)

    def test_resolve_failed_is_false(self):
        self.trigger.resolve(failed=False)
        self.assertEqual(self.invoke.call_count, 1)

    def test_resolve_failed_is_false_and_on_success_is_false(self):
        self.trigger = trigger('task', on_success=False)
        self.trigger.resolve(failed=False)
        self.assertEqual(self.invoke.call_count, 0)

    def test_resolve_failed_is_true(self):
        self.trigger.resolve(failed=True)
        self.assertEqual(self.invoke.call_count, 0)

    def test_resolve_failed_is_true_and_on_fail_is_true(self):
        self.trigger = trigger('task', on_fail=True)
        self.trigger.resolve(failed=True)
        self.assertEqual(self.invoke.call_count, 1)
