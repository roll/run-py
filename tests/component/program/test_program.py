import unittest
from unittest.mock import Mock
from run.program.program import Program


class ProgramTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Program = self._make_mock_program_class()
        self.program = self.Program('argv')

    def test___call__(self):
        self.program()
        self.program._Machine.assert_called_with(
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively',
            plain='plain',
            skip='skip',
            compact='compact')
        self.program._Machine.return_value.process.assert_called_with(
            self.program._command.task,
            *self.program._command.args,
            **self.program._command.kwargs)

    # Protected

    def _make_mock_program_class(self):
        class MockProgram(Program):
            # Protected
            _Command = Mock(return_value=Mock(
                task='task',
                args=('arg1',),
                kwargs={'kwarg1': 'kwarg1'},
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
