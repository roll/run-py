import unittest
from unittest.mock import Mock, patch
from run.task import converter


class task_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.isfunction = patch('inspect.isfunction').start()
        self.MethodTask = patch.object(converter, 'MethodTask').start()
        self.converter = self._make_mock_converter()

    def test(self):
        result = self.converter('method')
        self.assertEqual(result, self.MethodTask.return_value)
        # Check MethodTask call
        self.MethodTask.assert_called_with('method')

    def test_already_prototype(self):
        prototype = Mock(spec=[])
        result = self.converter(prototype)
        self.assertEqual(result, prototype)
        # Check MethodTask call
        self.assertFalse(self.MethodTask.called)

    def test_already_task(self):
        task = Mock(spec=[])
        result = self.converter(task)
        self.assertEqual(result, task)
        # Check MethodTask call
        self.assertFalse(self.MethodTask.called)

    def test_with_kwargs(self):
        result = self.converter(**self.kwargs)('method')
        self.assertEqual(result, self.MethodTask.return_value)
        # Check MethodTask call
        self.MethodTask.assert_called_with('method', **self.kwargs)

    # Protected

    def _make_mock_converter(self):
        class mock_converter(converter.task):
            # Protected
            _Task = Mock
            _TaskPrototype = Mock
        return mock_converter
