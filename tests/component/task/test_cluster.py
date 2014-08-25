import unittest
from unittest.mock import Mock
from run.task.cluster import ClusterTask


class ClusterTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.nested_task1 = Mock()
        self.nested_task2 = Mock()
        self.task = ClusterTask(
            [self.nested_task1, self.nested_task2], meta_module=None)

    def test___call__(self):
        self.assertEqual(
            self.task(*self.args, **self.kwargs),
            [self.nested_task1.return_value,
             self.nested_task2.return_value])
        # Check nested tasks calls
        self.nested_task1.assert_called_with(*self.args, **self.kwargs)
        self.nested_task2.assert_called_with(*self.args, **self.kwargs)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)
