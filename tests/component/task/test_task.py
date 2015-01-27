import unittest
from functools import partial
from importlib import import_module
from unittest.mock import Mock, call, patch
component = import_module('run.task.task')


class TaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.module = Mock()
        self.update = Mock()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.Task = self.make_task_class()
        self.pTask = partial(self.Task, Build=True, Updates=[self.update])
        self.task = self.pTask(*self.args, **self.kwargs)

    # Helpers

    def make_task_class(self):
        class Task(component.Task):
            """docstring"""
            # Public
            Invoke = Mock(return_value='value')
        return Task

    # Tests

    def test(self):
        # Check update.apply call
        self.update.apply.assert_called_with(self.task)

    def test___get__(self):
        self.assertEqual(self.task.__get__('module'), self.task)

    @unittest.skip
    @patch.object(component, 'TaskEvent')
    def test___call__(self, TaskEvent):
        self.Task.Dispatcher = Mock()
        self.assertEqual(self.task(), 'value')
        # Check Invoke call
        self.task.Invoke.assert_called_with(*self.args, **self.kwargs)
        # Check TaskEvent call
        TaskEvent.assert_has_calls(
            [call(self.task, event='called'),
             call(self.task, event='successed')])
        # Check dispatcher.add_event call
        self.task.Dispatcher.add_event.assert_has_calls(
            [call(TaskEvent.return_value),
             call(TaskEvent.return_value)])

    @unittest.skip
    @patch.object(component, 'TaskEvent')
    def test___call___with_Invoke_exception(self, TaskEvent):
        self.Task.Dispatcher = Mock()
        self.Task.Invoke.side_effect = Exception()
        self.assertRaises(Exception, self.task)
        # Check TaskEvent call
        TaskEvent.assert_has_calls(
            [call(self.task, event='called'),
             call(self.task, event='fail')])
        # Check dispatcher.add_event call
        self.task.Dispatcher.add_event.assert_has_calls(
            [call(TaskEvent.return_value),
             call(TaskEvent.return_value)])

    def test___call___with_Invoke_exception_and_Fallback(self):
        self.Task.Invoke.side_effect = Exception()
        self.Task.Fallback = 'fallback'
        self.assertEqual(self.task(), 'fallback')

    def test___call___with_dependencies(self):
        dependency = Mock()
        self.task.Depend(dependency)
        self.assertEqual(self.task(), 'value')
        # Check dependnecy resolve call
        dependency.resolve.assert_has_calls([
            call(fail=None),
            call(fail=False)])

    def test___call___with_dependencies_and_Invoke_exception(self):
        dependency = Mock()
        self.task.Depend(dependency)
        self.task.Invoke.side_effect = Exception()
        self.assertRaises(Exception, self.task)
        # Check dependnecy resolve call
        dependency.resolve.assert_has_calls([
            call(fail=None),
            call(fail=True)])

    def test___call___with_Chdir_is_false(self):
        self.Task.Chdir = False
        self.assertEqual(self.task(), 'value')

    def test___repr__(self):
        self.assertEqual(repr(self.task), '<Task>')

    def test___repr___with_Module(self):
        self.Task.Module = self.module
        self.module.Qualname = 'module'
        self.module.Tasks = {'task': self.task}
        self.assertEqual(repr(self.task), '<Task "module.task">')

    def test_Args(self):
        self.assertEqual(self.task.Args, self.args)

    def test_Basedir(self):
        self.assertEqual(self.task.Basedir, None)

    def test_Chdir(self):
        self.assertEqual(self.task.Chdir, component.settings.chdir)

    def test_Dependencies(self):
        self.assertEqual(self.task.Dependencies, [])

    def test_Depend(self):
        dependency = Mock()
        self.task.Depend(dependency)
        self.assertEqual(self.task.Dependencies, [dependency])
        # Check dependency's bind call
        dependency.bind.assert_called_with(self.task)

    @patch.object(component, 'trigger')
    @patch.object(component, 'require')
    def test_Dependencies_initter(self, require, trigger):
        dependency = Mock()
        self.task = self.pTask(
            Depend=[dependency],
            Require=['require'],
            Trigger=['trigger'])
        self.assertEqual(
            self.task.Dependencies,
            [dependency,
             require.return_value,
             trigger.return_value])
        # Check require, trigger call
        require.assert_called_with('require')
        trigger.assert_called_with('trigger')
        # Check dependency's bind call
        dependency.bind.assert_called_with(self.task)
        require.return_value.bind.assert_called_with(self.task)
        trigger.return_value.bind.assert_called_with(self.task)

    @unittest.skip
    def test_Dispatcher(self):
        self.assertEqual(self.task.Dispatcher, None)

    def test_Docstring(self):
        self.assertEqual(self.task.Docstring,
                         self.task.__doc__)

    def test_Fallback(self):
        self.assertEqual(self.task.Fallback, component.settings.fallback)

    def test_Kwargs(self):
        self.assertEqual(self.task.Kwargs, self.kwargs)

    def test_Main(self):
        self.assertIs(self.task.Main, self.task)

    def test_Main_with_Module(self):
        self.Task.Main = self.module
        self.assertEqual(self.task.Main, self.module)

    def test_Module(self):
        self.assertIsNone(self.task.Module)

    def test_Module_with_Module(self):
        self.task = self.Task(Build=True, Module=self.module)
        self.assertEqual(self.task.Module, self.module)

    def test_Name(self):
        self.assertEqual(self.task.Name, '')

    def test_Name_with_Module(self):
        self.Task.Module = self.module
        self.module.Tasks = {'task': self.task}
        self.assertEqual(self.task.Name, 'task')

    def test_NotDepend(self):
        dependency1 = Mock()
        dependency1.predecessor = 'task1'
        dependency2 = Mock()
        dependency2.predecessor = 'task2'
        self.Task.Dependencies = [dependency1, dependency2]
        self.task = self.Task(Build=True, Module=self.module)
        self.task.Module.task1 = 'task1'
        self.task.NotDepend('task1')
        self.assertEqual(self.task.Dependencies, [dependency2])

    def test_Qualname(self):
        self.assertEqual(self.task.Qualname, '')

    def test_Qualname_with_Module(self):
        self.Task.Module = self.module
        self.module.Qualname = 'module'
        self.module.Tasks = {'task': self.task}
        self.assertEqual(self.task.Qualname, 'module.task')

    @patch.object(component, 'require')
    def test_Require(self, require):
        self.task.Require('task', *self.args, **self.kwargs)
        self.assertEqual(self.task.Dependencies, [require.return_value])
        # Check require call
        require.assert_called_with('task', *self.args, **self.kwargs)
        # Check require's return_value (require dependency) bind call
        require.return_value.bind.assert_called_with(self.task)

    def test_Signature(self):
        self.assertEqual(self.task.Signature, '(*args, **kwargs)')

    def test_Style(self):
        self.assertEqual(self.task.Style, 'task')

    @patch.object(component, 'trigger')
    def test_Trigger(self, trigger):
        self.task.Trigger('task', *self.args, **self.kwargs)
        self.assertEqual(self.task.Dependencies, [trigger.return_value])
        # Check trigger call
        trigger.assert_called_with('task', *self.args, **self.kwargs)
        # Check trigger's return_value (trigger dependency) bind call
        trigger.return_value.bind.assert_called_with(self.task)

    def test_Type(self):
        self.assertEqual(self.task.Type, 'Task')
