import unittest
from functools import partial
from unittest.mock import Mock, call
from run.task.task import Task


class TaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.module = Mock()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.Task = self._make_mock_task_class()
        self.pTask = partial(self.Task, meta_module=None)
        self.task = self.pTask(*self.args, **self.kwargs)

    def test___get__(self):
        self.assertEqual(self.task.__get__('module'), self.task)

    def test___get___with_meta_is_descriptor(self):
        self.Task.meta_is_descriptor = True
        self.task.meta_cache = False
        self.assertEqual(self.task.__get__('module'), 'value')
        self.assertEqual(self.task.__get__('module'), 'value')
        # Two calls because of caching is off
        self.assertEqual(self.task.meta_invoke.call_count, 2)

    def test___get___with_meta_is_descriptor_and_meta_cache(self):
        self.Task.meta_is_descriptor = True
        self.task.meta_cache = True
        self.assertEqual(self.task.__get__('module'), 'value')
        self.assertEqual(self.task.__get__('module'), 'value')
        # Only one call because of caching
        self.assertEqual(self.task.meta_invoke.call_count, 1)
        self.task.meta_invoke.assert_called_with(*self.args, **self.kwargs)
        # Check TaskSignal call
        self.task._meta_TaskSignal.assert_has_calls(
            [call(self.task, event='called'),
             call(self.task, event='successed')])
        # Check dispatcher.add_signal call
        self.task.meta_dispatcher.add_signal.assert_has_calls(
            [call('signal'), call('signal')])

    def test___call__(self):
        self.assertEqual(self.task(), 'value')
        # Check meta_invoke call
        self.task.meta_invoke.assert_called_with(*self.args, **self.kwargs)
        # Check TaskSignal call
        self.task._meta_TaskSignal.assert_has_calls(
            [call(self.task, event='called'),
             call(self.task, event='successed')])
        # Check dispatcher.add_signal call
        self.task.meta_dispatcher.add_signal.assert_has_calls(
            [call('signal'), call('signal')])

    def test___call___with_meta_invoke_exception(self):
        self.task.meta_invoke.side_effect = Exception()
        self.assertRaises(Exception, self.task)
        # Check TaskSignal call
        self.task._meta_TaskSignal.assert_has_calls(
            [call(self.task, event='called'),
             call(self.task, event='failed')])
        # Check dispatcher.add_signal call
        self.task.meta_dispatcher.add_signal.assert_has_calls(
            [call('signal'), call('signal')])

    def test___call___with_meta_invoke_exception_and_meta_fallback(self):
        self.task.meta_invoke.side_effect = Exception()
        self.task.meta_fallback = 'fallback'
        self.assertEqual(self.task(), 'fallback')

    def test___call___with_dependencies(self):
        dependency = Mock()
        self.task.meta_depend(dependency)
        self.assertEqual(self.task(), 'value')
        # Check dependnecy resolve call
        dependency.resolve.assert_has_calls([
            call(failed=None),
            call(failed=False)])

    def test___call___with_dependencies_and_meta_invoke_exception(self):
        dependency = Mock()
        self.task.meta_depend(dependency)
        self.task.meta_invoke.side_effect = Exception()
        self.assertRaises(Exception, self.task)
        # Check dependnecy resolve call
        dependency.resolve.assert_has_calls([
            call(failed=None),
            call(failed=True)])

    def test___call___with_meta_chdir_is_false(self):
        self.task.meta_chdir = False
        self.assertEqual(self.task(), 'value')

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

    def test_meta_depend(self):
        dependency = Mock()
        self.task.meta_depend(dependency)
        self.assertEqual(self.task.meta_dependencies, [dependency])
        # Check dependency's bind call
        dependency.bind.assert_called_with(self.task)

    def test_meta_dependencies(self):
        self.assertEqual(self.task.meta_dependencies, [])

    def test_meta_dependencies_initter(self):
        dependency = Mock()
        self.task = self.pTask(
            meta_depend=[dependency],
            meta_require=['require'],
            meta_trigger=['trigger'])
        self.assertEqual(self.task.meta_dependencies, [
            dependency,
            self.task._meta_require.return_value,
            self.task._meta_trigger.return_value])
        # Check require, trigger call
        self.task._meta_require.assert_called_with('require')
        self.task._meta_trigger.assert_called_with('trigger')
        # Check dependency's bind call
        require = self.task._meta_require.return_value
        trigger = self.task._meta_trigger.return_value
        dependency.bind.assert_called_with(self.task)
        require.bind.assert_called_with(self.task)
        trigger.bind.assert_called_with(self.task)

    def test_meta_disable_dependency(self):
        dependency = Mock()
        dependency.predecessor = 'task'
        self.module.meta_lookup.return_value = 'task'
        self.task = self.Task(meta_module=self.module)
        self.task.meta_depend(dependency)
        self.task.meta_disable_dependency('task', types=[Mock])
        # Check dependency disable call
        self.assertTrue(dependency.disable.called)

    def test_meta_disable_dependency_with_different_task(self):
        dependency = Mock()
        dependency.predecessor = 'task'
        self.module.meta_lookup.return_value = 'different_task'
        self.task = self.Task(meta_module=self.module)
        self.task.meta_depend(dependency)
        self.task.meta_disable_dependency('different_task', types=[Mock])
        # Check dependency disable call
        self.assertFalse(dependency.disable.called)

    def test_meta_enable_dependency(self):
        dependency = Mock()
        dependency.predecessor = 'task'
        self.module.meta_lookup.return_value = 'task'
        self.task = self.Task(meta_module=self.module)
        self.task.meta_depend(dependency)
        self.task.meta_enable_dependency('task', types=[Mock])
        # Check dependency enable call
        self.assertTrue(dependency.enable.called)

    def test_meta_enable_dependency_with_different_task(self):
        dependency = Mock()
        dependency.predecessor = 'task'
        self.module.meta_lookup.return_value = 'different_task'
        self.task = self.Task(meta_module=self.module)
        self.task.meta_depend(dependency)
        self.task.meta_enable_dependency('different_task', types=[Mock])
        # Check dependency enable call
        self.assertFalse(dependency.enable.called)

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

    def test_meta_require(self):
        self.task.meta_require('task', *self.args, **self.kwargs)
        self.assertEqual(
            self.task.meta_dependencies,
            [self.task._meta_require.return_value])
        # Check require call
        self.task._meta_require.assert_called_with(
            'task', *self.args, **self.kwargs)
        # Check require's return_value (require dependency) bind call
        require = self.task._meta_require.return_value
        require.bind.assert_called_with(self.task)

    def test_meta_trigger(self):
        self.task.meta_trigger('task', *self.args, **self.kwargs)
        self.assertEqual(
            self.task.meta_dependencies,
            [self.task._meta_trigger.return_value])
        # Check trigger call
        self.task._meta_trigger.assert_called_with(
            'task', *self.args, **self.kwargs)
        # Check trigger's return_value (trigger dependency) bind call
        trigger = self.task._meta_trigger.return_value
        trigger.bind.assert_called_with(self.task)

    # Protected

    def _make_mock_task_class(self):
        class MockTask(Task):
            # Public
            meta_dispatcher = Mock()
            meta_invoke = Mock(return_value='value')
            # Protected
            _meta_require = Mock()
            _meta_trigger = Mock()
            _meta_TaskSignal = Mock(return_value='signal')
        return MockTask
