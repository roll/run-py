import unittest
from unittest.mock import Mock, call
from run.machine.machine import Machine


class MachineTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1', }
        self.task = Mock()
        self.module = Mock(attribute='attribute', task=self.task)
        self.Module = Mock(return_value=self.module)
        self.Machine = self._make_mock_machine_class(self.Module)

    def test_run(self):
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
        self.machine.run('task', *self.args, **self.kwargs)
        # Check find call
        self.machine._find.assert_called_with(
            target=self.machine._Module,
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively')
        # Check Dispatcher call
        self.machine._Dispatcher.assert_called_with()
        # Check Module call
        self.Module.assert_called_with(
            meta_dispatcher=self.machine._Dispatcher.return_value,
            meta_plain='plain',
            meta_module=None)
        # Check task call
        self.task.assert_called_with(*self.args, **self.kwargs)
        # Check stack
        self.assertEqual(self.machine._stack, self.machine._Stack.return_value)
        self.assertTrue(self.machine._Stack.called)
        # Check print call
        self.machine._print.assert_has_calls([
            call(self.task.return_value)])

    # Protected

    def _make_mock_machine_class(self, module_class):
        class MockMachine(Machine):
            # Protected
            _Controller = Mock()
            _Dispatcher = Mock(return_value=Mock(add_handler=Mock()))
            _find = Mock(return_value=[module_class])
            _print = Mock()
            _Stack = Mock()
            _Task = Mock
        return MockMachine
