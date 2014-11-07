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
        self.MethodTask = patch.object(component, 'MethodTask').start()

    # Tests

    def test(self):
        result = component.task('method')
        self.assertEqual(result, self.MethodTask.return_value)
        # Check MethodTask call
        self.MethodTask.assert_called_with('method')

    def test_with_kwargs(self):
        result = component.task(**self.kwargs)('method')
        self.assertEqual(result, self.MethodTask.return_value)
        # Check MethodTask call
        self.MethodTask.assert_called_with('method', **self.kwargs)

    def test_with_staticmethod_object(self):
        self.assertRaises(component.ConversionError,
            component.task, staticmethod(print))

    def test_with_classmethod_object(self):
        self.assertRaises(component.ConversionError,
            component.task, classmethod(print))
