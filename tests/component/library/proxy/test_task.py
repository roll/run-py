import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.library.proxy.task')


@unittest.skip
class ProxyTaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.task = component.ProxyTask('task', meta_module=None)
        self.task.meta_module.task = Mock()

    # Tests

    def test___call__(self):
        self.assertEqual(
            self.task(*self.args, **self.kwargs),
            self.task.meta_module.task.return_value)
        # Check task call
        self.task.meta_module.task.assert_called_with(
            *self.args, **self.kwargs)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)

    def test_meta_signature(self):
        self.assertTrue(self.task.meta_signature)
