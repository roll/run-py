import unittest
from unittest.mock import patch
from importlib import import_module
component = import_module('run.task.converter')


class task_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.isfunction = patch('inspect.isfunction').start()
        self.FunctionTask = patch.object(component, 'FunctionTask').start()

    # Tests

    def test(self):
        result = component.task('method')
        self.assertEqual(result, self.FunctionTask.return_value)
        # Check FunctionTask call
        self.FunctionTask.assert_called_with('method', bind=True)

    def test_with_kwargs(self):
        result = component.task(**self.kwargs)('method')
        self.assertEqual(result, self.FunctionTask.return_value)
        # Check FunctionTask call
        self.FunctionTask.assert_called_with('method', bind=True, **self.kwargs)
