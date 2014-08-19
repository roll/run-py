import unittest
from unittest.mock import patch
from run.task import converter


class task_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.isfunction = patch('inspect.isfunction').start()
        self.MethodTask = patch.object(converter, 'MethodTask').start()

    def test(self):
        result = converter.task('method')
        self.assertEqual(result, self.MethodTask.return_value)
        # Check MethodTask call
        self.MethodTask.assert_called_with('method')

    def test_with_kwargs(self):
        result = converter.task(**self.kwargs)('method')
        self.assertEqual(result, self.MethodTask.return_value)
        # Check MethodTask call
        self.MethodTask.assert_called_with('method', **self.kwargs)
