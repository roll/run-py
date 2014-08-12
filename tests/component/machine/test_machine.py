import unittest
from unittest.mock import Mock, call
from run.machine.machine import Machine


class MachineTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1', }
        self.Machine = self._make_mock_machine_class()

    def test_process(self):
        machine = self.Machine(
            names='names',
            tags='tags',
            file='file',
            basedir='basedir',
            recursively='recursively',
            plain='plain',
            skip='skip')
        machine.process('task', *self.args, **self.kwargs)
        # Check print call
        machine._print.assert_has_calls([
            call('result1'),
            call('result2'),
            call('attr3')])
        # Check Controller call
        machine._Controller.assert_called_with(
            machine._Dispatcher.return_value,
            machine._Stack.return_value)
        # Check ModuleCluster call
        machine._ModuleCluster.assert_called_with(
            names='names',
            tags='tags',
            file='file',
            basedir='basedir',
            recursively='recursively',
            plain='plain',
            skip='skip',
            dispatcher=machine._Dispatcher.return_value)
        # Check Cluster's return values
        for attr in machine._ModuleCluster.return_value.task:
            if hasattr(attr, 'assert_called_with'):
                attr.assert_called_with(*self.args, **self.kwargs)
        # Check Dispatcher callCluster
        machine._Dispatcher.assert_called_with()
        # Check stack
        self.assertEqual(machine._stack, machine._Stack.return_value)
        self.assertTrue(machine._Stack.called)

    def test_process_with_compact_is_true(self):
        machine = self.Machine(compact=True)
        # Stack
        self.assertEqual(machine._stack, None)
        self.assertFalse(machine._Stack.called)

    # Protected

    def _make_mock_machine_class(self):
        class MockMachine(Machine):
            # Protected
            _Controller = Mock()
            _Dispatcher = Mock(return_value=Mock(add_handler=Mock()))
            _ModuleCluster = Mock(return_value=Mock(task=[
                Mock(return_value='result1'),
                Mock(return_value='result2'),
                'attr3']))
            _print = Mock()
            _Stack = Mock()
            _Task = Mock
        return MockMachine
