import unittest
from unittest.mock import patch
from run.var.var_function import var

class var_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.property = patch('builtins.property').start()
        self.task_class = patch.object(var, '_task_class').start()
        self.kwargs = {'kwarg1': 'kwarg1'}

    def test(self):
        result = var('method')
        self.assertEqual(result, self.task_class.return_value)
        # Check property call
        self.property.assert_called_with('method')
        # Check task_class call
        self.task_class.assert_called_with(self.property.return_value)

    def test_with_kwargs(self):
        result = var(**self.kwargs)('method')
        self.assertEqual(result, self.task_class.return_value)
        # Check property call
        self.property.assert_called_with('method')
        # Check task_class call
        self.task_class.assert_called_with(
            self.property.return_value, **self.kwargs)
