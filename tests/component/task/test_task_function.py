import unittest
from unittest.mock import patch
from run.task.task_function import task

class task_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.task_class = patch.object(task, '_task_class').start()
        self.kwargs = {'kwarg1': 'kwarg1'}

    def test(self):
        result = task('method')
        self.assertEqual(result, self.task_class.return_value)
        # Check task_class call
        self.task_class.assert_called_with('method')

    def test_with_kwargs(self):
        result = task(**self.kwargs)('method')
        self.assertEqual(result, self.task_class.return_value)
        # Check task_class call
        self.task_class.assert_called_with('method', **self.kwargs)
