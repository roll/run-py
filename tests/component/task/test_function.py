import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.function')


class FunctionTaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.function = Mock(__doc__='__doc__')
        self.task = component.FunctionTask(self.function, meta_module=None)

    # Tests

    def test___call__(self):
        result = self.task(*self.args, **self.kwargs)
        self.assertEqual(result, self.function.return_value)
        self.function.assert_called_with(*self.args, **self.kwargs)

    def test_meta_docstring(self):
        self.assertEqual(self.task.meta_docstring, self.function.__doc__)

    def test_meta_signature(self):
        self.assertEqual(self.task.meta_signature, '(*args, **kwargs)')
