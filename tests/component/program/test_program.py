import unittest
from unittest.mock import Mock
from run.program.program import Program

class ProgramTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.MockProgram = self._make_mock_program_class()
        self.program = self.MockProgram('argv')

    def test___call__(self):
        self.program()
        self.program._machine_class.assert_called_with(
            names='names',
            tags='tags',
            file='file',
            basedir='basedir',
            recursively='recursively',
            skip='skip',
            plain='plain')
        self.program._machine_class.return_value.process.assert_called_with(
            self.program._command.task,
            *self.program._command.args,
            **self.program._command.kwargs)

    # Protected

    def _make_mock_program_class(self):
        class MockProgram(Program):
            # Protected
            _command_class = Mock(return_value=Mock(
                task='task',
                args=('arg1',),
                kwargs={'kwarg1': 'kwarg1'},
                debug='debug',
                verbose='verbose',
                quiet='quiet',
                names='names',
                tags='tags',
                basedir='basedir',
                file='file',
                recursively='recursively',
                skip='skip',
                plain='plain'))
            _machine_class = Mock()
        return MockProgram
