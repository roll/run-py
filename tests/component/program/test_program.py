import inspect
import unittest
from unittest.mock import Mock, patch
from run.program.program import Program
program = inspect.getmodule(Program)


class ProgramTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.Machine = Mock()
        patch.object(program, 'Machine', self.Machine).start()
        self.Program = self._make_mock_program_class()
        self.program = self.Program('argv')

    def test___call__(self):
        self.program()
        # Check Machine call
        self.Machine.assert_called_with(
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively',
            plain='plain',
            skip='skip',
            compact='compact')
        # Check Machine's return value call
        self.Machine.return_value.run.assert_called_with(
            self.program._command.attribute,
            *self.program._command.arguments['args'],
            **self.program._command.arguments['kwargs'])

    # Protected

    def _make_mock_program_class(self):
        class MockProgram(program.Program):
            # Protected
            _Command = Mock(return_value=Mock(
                attribute='attribute',
                arguments={'args': ('arg1',), 'kwargs': {'kwarg1': 'kwarg1'}},
                debug='debug',
                verbose='verbose',
                quiet='quiet',
                tags='tags',
                basedir='basedir',
                compact='compact',
                exclude='exclude',
                file='file',
                key='key',
                recursively='recursively',
                plain='plain',
                skip='skip'))
            _Machine = Mock()
        return MockProgram
