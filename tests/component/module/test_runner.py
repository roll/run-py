import unittest
from unittest.mock import Mock, call, patch
from importlib import import_module
component = import_module('run.module.runner')


@unittest.skip
class MachineTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1', }
        self.callable = Mock()
        self.Signal = self.make_mock_signal_class()
        self.Stack = self.make_mock_stack_class()
        self.logging = patch.object(component, 'logging').start()
        self.logger = self.logging.getLogger.return_value
        self.module = Mock(callable=self.callable, not_callable='not_callable')
        self.Module = Mock(return_value=self.module)
        self.Machine = self.make_mock_machine_class(self.Module, self.Stack)
        self.machine = self.Machine()

    # Helpers

    def make_mock_signal_class(self):
        class MockSignal:
            # Public
            def __init__(self, task, event):
                self.task = task
                self.event = event
            def format(self):
                return self.event + '_'
        return MockSignal

    def make_mock_stack_class(self):
        class MockStack(list):
            # Public
            def push(self, task):
                self.append(task)
            def format(self):
                return '.'.join(self)
        return MockStack

    def make_mock_machine_class(self, module_class, stack_class):
        class MockMachine(component.Machine):
            _Controller = Mock()
            _find = Mock(return_value=[module_class])
            _print = Mock()
            _Stack = stack_class
            _Task = Mock
        return MockMachine

    # Tests

    def test_run_callable(self):
        self.machine = self.Machine(
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively',
            compact='compact',
            skip='skip',
            plain='plain')
        self.machine.run('callable', *self.args, **self.kwargs)
        # Check find call
        self.machine._find.assert_called_with(
            target=self.machine._Module,
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively')
        # Check Module call
        self.Module.assert_called_with(
            meta_plain='plain',
            meta_module=None)
        # Check callable call
        self.callable.assert_called_with(*self.args, **self.kwargs)
        # Check print call
        self.machine._print.assert_has_calls([
            call(self.callable.return_value)])

    def test_run_not_callable(self):
        self.machine.run('not_callable')
        # Check print call
        self.machine._print.assert_has_calls([
            call('not_callable')])

    def test_run_with_not_existent_attribute(self):
        self.module.mock_add_spec([])
        self.assertRaises(AttributeError, self.machine.run, 'not_existent')

    def test_run_with_not_existent_attribute_and_skip_is_true(self):
        self.machine = self.Machine(skip=True)
        self.module.mock_add_spec([])
        self.machine.run('not_existent')
        # Check print call
        self.assertFalse(self.machine._print.called)

    def test__on_task_signal(self):
        self.signal = self.Signal('task', 'event')
        self.machine._on_task_signal(self.signal)
        self.logger.info.assert_called_with('event_')

    def test__on_task_signal_with_compact_is_true(self):
        self.machine = self.Machine(compact=True)
        self.signal = self.Signal('task', 'event')
        self.machine._on_task_signal(self.signal)
        self.logger.info.assert_called_with('event_task')
        self.assertEqual(self.machine._stack, [])

    def test__on_task_signal_with_event_is_called_then_successed(self):
        # Signal is called
        self.signal = self.Signal('task', 'called')
        self.machine._on_task_signal(self.signal)
        self.logger.info.assert_called_with('called_task')
        self.assertEqual(self.machine._stack, ['task'])
        # Signal is successed
        self.signal = self.Signal('task', 'successed')
        self.machine._on_task_signal(self.signal)
        self.logger.info.assert_called_with('successed_task')
        self.assertEqual(self.machine._stack, [])
