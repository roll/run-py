import unittest
from unittest.mock import patch
from run.dependency.depend import depend

class depend_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.MethodTask = patch.object(depend, '_method_task_class').start()

    def test___call__(self):
        result = depend('dependency')('method')
        self.assertEqual(result, self.MethodTask.return_value)
        # MethodTask call check
        self.MethodTask.assert_called_with('method')
        # MethodTask's return value (prototype) call check
        self.MethodTask.return_value.depend.assert_called_with('dependency')
