import unittest
from unittest.mock import Mock, patch
from run.dependency.require import require

class require_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.MethodTask = patch.object(require, '_method_task_class').start()

    def test___call__(self):
        pass

    def test_resolve(self):
        pass
