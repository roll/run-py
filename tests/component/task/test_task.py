import unittest
from functools import partial
from unittest.mock import Mock, call
from run.task.task import Task

class TaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.MockTask = self._make_mock_task_class()
        self.ptask = partial(self.MockTask, meta_module=None)
        self.task = self.ptask()

    def test___get__(self):
        self.assertEqual(self.task.__get__('module'), self.task)

    def test___set__(self):
        value = lambda: 'value'
        self.task.__set__('module', value)
        self.assertEqual(self.task.invoke, value)

    def test___set___not_callable(self):
        self.assertRaises(TypeError, self.task.__set__, 'module', 'value')

    def test___call__(self):
        self.assertEqual(self.task.__call__(), 'value')
        self.task.invoke.assert_called_with()
        self.task._initiated_signal_class.assert_called_with(self.task)
        self.task._successed_signal_class.assert_called_with(self.task)
        self.task.meta_dispatcher.add_signal.assert_has_calls(
            [call('initiated_signal'), call('successed_signal')])

    def test_meta_basedir(self):
        self.assertEqual(self.task.meta_basedir,
                         self.task.meta_module.meta_basedir)

    def test_meta_basedir_setter(self):
        self.task.meta_basedir = 'basedir'
        self.assertEqual(self.task.meta_basedir, 'basedir')

    def test_meta_signature(self):
        self.assertEqual(self.task.meta_signature, '(*args, **kwargs)')

    # Protected

    def _make_mock_task_class(self):
        class MockTask(Task):
            # Public
            invoke = Mock(return_value='value')
            meta_dispatcher = Mock(add_signal=Mock())
            # Protected
            _initiated_signal_class = Mock(return_value='initiated_signal')
            _successed_signal_class = Mock(return_value='successed_signal')
        return MockTask
