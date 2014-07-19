import unittest
from unittest.mock import Mock, patch
from run.dependency.trigger import trigger

class trigger_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.MethodTask = patch.object(trigger, '_method_task_class').start()

    def test___call__(self):
        pass

    def test_resolve(self):
        pass
