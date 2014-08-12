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
            names='names',
            tags='tags',
            file='file',
            basedir='basedir',
            recursively='recursively',
            grayscale='grayscale',
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
                names='names',
                tags='tags',
                basedir='basedir',
                file='file',
                recursively='recursively',
                grayscale='grayscale',
                skip='skip',
                compact='compact'))
            _Machine = Mock()
        return MockProgram
