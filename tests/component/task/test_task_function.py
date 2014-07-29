import unittest
from unittest.mock import Mock, patch
from run.task import task_function

class task_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.MethodTask = patch.object(task_function, 'MethodTask').start()
        self.task = self._make_mock_task()

    def test(self):
        result = self.task('method')
        self.assertEqual(result, self.MethodTask.return_value)
        # Check MethodTask call
        self.MethodTask.assert_called_with('method')

    def test_already_prototype(self):
        prototype = Mock()
        result = self.task(prototype)
        self.assertEqual(result, prototype)
        # Check MethodTask call
        self.assertFalse(self.MethodTask.called)

    def test_already_task(self):
        task = Mock()
        result = self.task(task)
        self.assertEqual(result, task)
        # Check MethodTask call
        self.assertFalse(self.MethodTask.called)

    def test_with_kwargs(self):
        result = self.task(**self.kwargs)('method')
        self.assertEqual(result, self.MethodTask.return_value)
        # Check MethodTask call
        self.MethodTask.assert_called_with('method', **self.kwargs)

    # Protected

    def _make_mock_task(self):
        class mock_task(task_function.task):
            # Protected
            _task_class = Mock
            _task_prototype_class = Mock
        return mock_task
