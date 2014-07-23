import unittest
from functools import partial
from unittest.mock import Mock, call
from run.task.task import Task

class TaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.MockTask = self._make_mock_task_class()
        self.pTask = partial(self.MockTask, meta_module=None)
        self.task = self.pTask(*self.args, **self.kwargs)

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
        self.task.invoke.assert_called_with(*self.args, **self.kwargs)
        self.task._initiated_signal_class.assert_called_with(self.task)
        self.task._successed_signal_class.assert_called_with(self.task)
        self.task.meta_dispatcher.add_signal.assert_has_calls(
            [call('initiated_signal'), call('successed_signal')])

    def test_meta_args(self):
        self.assertEqual(self.task.meta_args, self.args)

    def test_meta_basedir(self):
        self.assertEqual(self.task.meta_basedir,
                         self.task.meta_module.meta_basedir)

    def test_meta_basedir_setter(self):
        self.task.meta_basedir = 'basedir'
        self.assertEqual(self.task.meta_basedir, 'basedir')

    def test_meta_chdir(self):
        self.assertEqual(self.task.meta_chdir,
                         self.task.meta_module.meta_chdir)

    def test_meta_chdir_setter(self):
        self.task.meta_chdir = 'chdir'
        self.assertEqual(self.task.meta_chdir, 'chdir')

    def test_meta_dependencies(self):
        dependency = Mock()
        task = self.pTask(depend=[dependency])
        self.assertEqual(task.meta_dependencies, [dependency])
        # Check dependency's bind call
        dependency.bind.assert_called_with(task)

    def test_meta_fallback(self):
        self.assertEqual(self.task.meta_fallback,
                         self.task.meta_module.meta_fallback)

    def test_meta_fallback_setter(self):
        self.task.meta_fallback = 'fallback'
        self.assertEqual(self.task.meta_fallback, 'fallback')

    def test_meta_kwargs(self):
        self.assertEqual(self.task.meta_kwargs, self.kwargs)

    def test_meta_signature(self):
        self.assertEqual(self.task.meta_signature, '(*args, **kwargs)')

    def test_meta_signature_setter(self):
        self.task.meta_signature = 'signature'
        self.assertEqual(self.task.meta_signature, 'signature')

    def test_meta_strict(self):
        self.assertEqual(self.task.meta_strict,
                         self.task.meta_module.meta_strict)

    def test_meta_strict_setter(self):
        self.task.meta_strict = 'strict'
        self.assertEqual(self.task.meta_strict, 'strict')

    def test_depend(self):
        dependency = Mock()
        self.task.depend(dependency)
        self.assertEqual(self.task.meta_dependencies, [dependency])
        # Check dependency's bind call
        dependency.bind.assert_called_with(self.task)

    def test_require(self):
        self.task.require('task', *self.args, **self.kwargs)
        self.assertEqual(
            self.task.meta_dependencies, [self.task._require.return_value])
        # Check require call
        self.task._require.assert_called_with(
            'task', *self.args, **self.kwargs)
        # Check require's return_value bind call
        self.task._require.return_value.bind.assert_called_with(self.task)

    # Protected

    def _make_mock_task_class(self):
        class MockTask(Task):
            # Public
            invoke = Mock(return_value='value')
            meta_dispatcher = Mock(add_signal=Mock())
            # Protected
            _initiated_signal_class = Mock(return_value='initiated_signal')
            _successed_signal_class = Mock(return_value='successed_signal')
            _require = Mock()
            _trigger = Mock()
        return MockTask
