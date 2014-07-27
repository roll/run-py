import unittest
from functools import partial
from unittest.mock import Mock, call
from run.task.task import Task

class TaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.Task = self._make_mock_task_class()
        self.pTask = partial(self.Task, meta_module=None)
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
        self.assertEqual(self.task(), self.task.invoke.return_value)
        # Check invoke call
        self.task.invoke.assert_called_with(*self.args, **self.kwargs)
        # Check signal call
        self.task._initiated_signal_class.assert_called_with(self.task)
        self.task._successed_signal_class.assert_called_with(self.task)
        # Check dispatcher call
        self.task.meta_dispatcher.add_signal.assert_has_calls(
            [call('initiated_signal'), call('successed_signal')])

    def test___call___with_invoke_exception(self):
        self.task.invoke.side_effect = Exception()
        self.assertRaises(Exception, self.task)
        # Check signal call
        self.task._initiated_signal_class.assert_called_with(self.task)
        self.task._failed_signal_class.assert_called_with(self.task)
        # Check dispatcher call
        self.task.meta_dispatcher.add_signal.assert_has_calls(
            [call('initiated_signal'), call('failed_signal')])

    def test___call___with_invoke_exception_and_meta_fallback(self):
        self.task.invoke.side_effect = Exception()
        self.task.meta_fallback = 'fallback'
        self.assertEqual(self.task(), 'fallback')

    def test___call___with_dependencies(self):
        dependency = Mock()
        self.task.depend(dependency)
        self.assertEqual(self.task(), self.task.invoke.return_value)
        # Check dependnecy resolve call
        dependency.resolve.assert_has_calls([
            call(failed=None),
            call(failed=False)])

    def test___call___with_dependencies_and_invoke_exception(self):
        dependency = Mock()
        self.task.depend(dependency)
        self.task.invoke.side_effect = Exception()
        self.assertRaises(Exception, self.task)
        # Check dependnecy resolve call
        dependency.resolve.assert_has_calls([
            call(failed=None),
            call(failed=True)])

    def test___call___with_meta_chdir_is_false(self):
        self.task.meta_chdir = False
        self.assertEqual(self.task(), self.task.invoke.return_value)

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
        self.assertEqual(self.task.meta_dependencies, [])

    def test_meta_dependencies_initter(self):
        dependency = Mock()
        self.Task._isinstance = Mock(return_value=False)
        self.task = self.pTask(
            depend=[dependency],
            require=['require'],
            trigger=['trigger'])
        self.assertEqual(self.task.meta_dependencies, [
            dependency,
            self.task._require.return_value,
            self.task._trigger.return_value])
        # Check require, trigger call
        self.task._require.assert_called_with('require')
        self.task._trigger.assert_called_with('trigger')
        # Check dependency's bind call
        dependency.bind.assert_called_with(self.task)
        self.task._require.return_value.bind.assert_called_with(self.task)
        self.task._trigger.return_value.bind.assert_called_with(self.task)

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

    def test_trigger(self):
        self.task.trigger('task', *self.args, **self.kwargs)
        self.assertEqual(
            self.task.meta_dependencies, [self.task._trigger.return_value])
        # Check trigger call
        self.task._trigger.assert_called_with(
            'task', *self.args, **self.kwargs)
        # Check trigger's return_value bind call
        self.task._trigger.return_value.bind.assert_called_with(self.task)

    def test_enable_dependency(self):
        dependency = Mock()
        dependency.task = 'task'
        self.task.depend(dependency)
        self.task.enable_dependency('task', category=Mock)
        # Check dependency enable call
        self.assertTrue(dependency.enable.called)

    def test_enable_dependency_with_different_task(self):
        dependency = Mock()
        dependency.task = 'task'
        self.task.depend(dependency)
        self.task.enable_dependency('different_task', category=Mock)
        # Check dependency enable call
        self.assertFalse(dependency.enable.called)

    def test_disable_dependency(self):
        dependency = Mock()
        dependency.task = 'task'
        self.task.depend(dependency)
        self.task.disable_dependency('task', category=Mock)
        # Check dependency disable call
        self.assertTrue(dependency.disable.called)

    def test_disable_dependency_with_different_task(self):
        dependency = Mock()
        dependency.task = 'task'
        self.task.depend(dependency)
        self.task.disable_dependency('different_task', category=Mock)
        # Check dependency disable call
        self.assertFalse(dependency.disable.called)

    # Protected

    def _make_mock_task_class(self):
        class MockTask(Task):
            # Public
            invoke = Mock()
            meta_dispatcher = Mock(add_signal=Mock())
            # Protected
            _failed_signal_class = Mock(return_value='failed_signal')
            _initiated_signal_class = Mock(return_value='initiated_signal')
            _require = Mock()
            _successed_signal_class = Mock(return_value='successed_signal')
            _trigger = Mock()
        return MockTask
