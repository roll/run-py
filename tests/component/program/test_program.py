import unittest
from unittest.mock import Mock, patch
from importlib import import_module
component = import_module('run.program.program')


class ProgramTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.Machine = Mock()
        patch.object(component, 'Machine', self.Machine).start()
        self.Program = self.make_mock_program_class()
        self.program = self.Program('argv')

    # Helpers

    def make_mock_program_class(self):
        class MockProgram(component.Program):
            # Protected
            _Command = Mock(return_value=Mock(
                attribute='attribute',
                arguments={'args': ('arg1',), 'kwargs': {'kwarg1': 'kwarg1'}},
                debug='debug',
                verbose='verbose',
                quiet='quiet',
                filepath='filepath',
                compact='compact',
                plain='plain'))
        return MockProgram

    # Tests

    def test___call__(self):
        self.program()
        # Check Machine call
        self.Machine.assert_called_with(
            filepath='filepath',
            compact='compact',
            plain='plain')
        # Check Machine's return value call
        self.Machine.return_value.run.assert_called_with(
            self.program._command.attribute,
            *self.program._command.arguments['args'],
            **self.program._command.arguments['kwargs'])
