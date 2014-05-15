import logging
import unittest
from unittest.mock import Mock, call, patch
from run.program import Program

class ProgramTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.MockProgram = self._make_mock_program_class()
        self.argv = 'argv'
        self.program = self.MockProgram(self.argv)
        
    def test___call__(self):
        program = Mock(_config=Mock(), _execute=Mock())
        self.MockProgram.__call__(program)
        program._config.assert_called_with()
        program._execute.assert_called_with()
    
    @patch('logging.config')
    @patch('logging.getLogger')
    def test_config(self, get_logger, logging_config):
        self.program._config()
        logging_config.dictConfig.assert_called_with(
            self.program._logging_config)
        get_logger.assert_called_with()
        get_logger.return_value.setLevel.assert_has_calls([
            call(logging.DEBUG),
            call(logging.INFO),
            call(logging.ERROR)])
        
    def test_execute(self):
        self.program._execute()
        (self.program._run_class.return_value.run.
            assert_called_with(
                self.program._command.attribute,
                *self.program._command.args,
                **self.program._command.kwargs))   
        
    def test_command(self):
        self.program._command
        self.program._command_class.assert_called_with(self.argv)
        
    def test_run(self):
        self.program._run
        self.program._run_class.assert_called_with(
            names='names',
            tags='tags',
            file='file',            
            basedir='basedir', 
            recursively='recursively',
            strict='strict',
            plain='plain')       
    
    #Protected
    
    def _make_mock_program_class(self):
        class MockProgram(Program):
            #Protected
            _logging_config = 'config'
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
                strict='strict',
                plain='plain'))
            _run_class = Mock(return_value=Mock(run=Mock()))
        return MockProgram