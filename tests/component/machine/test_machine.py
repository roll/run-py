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
            skip='skip')
        machine.process('attribute', *self.args, **self.kwargs)
        # Print
        machine._print.assert_has_calls([
            call('result1'),
            call('result2'),
            call('attr3')])
        # Controller
        machine._controller_class.assert_called_with(
            machine._dispatcher_class.return_value,
            machine._stack_class.return_value)
        # Cluster
        machine._cluster_class.assert_called_with(
            names='names',
            tags='tags',
            file='file',
            basedir='basedir',
            recursively='recursively',
            skip='skip',
            dispatcher=machine._dispatcher_class.return_value)
        # Cluster's return values
        for attr in machine._cluster_class.return_value.attribute:
            if hasattr(attr, 'assert_called_with'):
                attr.assert_called_with(*self.args, **self.kwargs)
        # Dispatcher
        machine._dispatcher_class.assert_called_with()
        # Stack
        self.assertEqual(machine._stack, machine._stack_class.return_value)
        self.assertTrue(machine._stack_class.called)

    def test_process_with_plain_is_true(self):
        machine = self.Machine(plain=True)
        # Stack
        self.assertEqual(machine._stack, None)
        self.assertFalse(machine._stack_class.called)

    # Protected

    def _make_mock_machine_class(self):
        class MockMachine(Machine):
            # Protected
            _controller_class = Mock()
            _dispatcher_class = Mock(return_value=Mock(add_handler=Mock()))
            _cluster_class = Mock(return_value=Mock(attribute=[
                Mock(return_value='result1'),
                Mock(return_value='result2'),
                'attr3']))
            _print = Mock()
            _stack_class = Mock()
            _task_class = Mock
        return MockMachine
