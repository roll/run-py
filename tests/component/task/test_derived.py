import unittest
from unittest.mock import Mock
from run.task.derived import DerivedTask

class DerivedTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.task = DerivedTask('task', meta_module=None)
        self.task.meta_module.task = Mock()

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
