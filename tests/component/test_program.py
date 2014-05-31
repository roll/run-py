import unittest
from unittest.mock import Mock
from run.program import Program

class ProgramTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.MockProgram = self._make_mock_program_class()
        self.program = self.MockProgram('argv')
        
    def test___call__(self):
        self.program()
        self.program._run_class.assert_called_with(
            names='names',
            tags='tags',
            file='file',            
            basedir='basedir', 
            recursively='recursively',
            existent='existent',
            plain='plain')          
        self.program._run_class.return_value.run.assert_called_with(
            self.program._command.attribute,
            *self.program._command.args,
            **self.program._command.kwargs)
    
    #Protected
    
    def _make_mock_program_class(self):
        class MockProgram(Program):
            #Protected
            _command_class = Mock(return_value=Mock(
                attribute='attribute',
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
                existent='existent',
                plain='plain'))
            _run_class = Mock()
        return MockProgram