import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.method')


class MethodTaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.method = Mock(__doc__='__doc__')
        self.task = component.MethodTask(self.method, Build=True)

    # Tests

    def test___call__(self):
        result = self.task(*self.args, **self.kwargs)
        self.assertEqual(result, self.method.return_value)
        self.method.assert_called_with(None, *self.args, **self.kwargs)

    def test_Docstring(self):
        self.assertEqual(self.task.Docstring, self.method.__doc__)

    def test_Signature(self):
        self.assertEqual(self.task.Signature, '(*args, **kwargs)')
