import unittest
from unittest.mock import patch
from run.frame.task import converter


class task_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.isfunction = patch('inspect.isfunction').start()
        self.FunctionTask = patch.object(converter, 'FunctionTask').start()

    def test(self):
        result = converter.task('method')
        self.assertEqual(result, self.FunctionTask.return_value)
        # Check FunctionTask call
        self.FunctionTask.assert_called_with('method', bind=True)

    def test_with_kwargs(self):
        result = converter.task(**self.kwargs)('method')
        self.assertEqual(result, self.FunctionTask.return_value)
        # Check FunctionTask call
        self.FunctionTask.assert_called_with('method', bind=True, **self.kwargs)
