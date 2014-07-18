import unittest
from unittest.mock import patch
from run.task import derived

class DerivedTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.attribute = patch.object(derived, 'attribute').start()
        self.task = derived.DerivedTask('task', meta_module=None)

    def test___call__(self):
        self.assertEqual(
            self.task(*self.args, **self.kwargs),
            self.attribute.return_value.return_value)
        # Check attribute call
        self.attribute.assert_called_with(
            self.task.meta_module, 'task',
            category=derived.Task, getvalue=True)
        # Check attribute's return value (task) call
        self.attribute.return_value.assert_called_with(
            *self.args, **self.kwargs)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)

    def test_meta_signature(self):
        self.assertTrue(self.task.meta_signature)
