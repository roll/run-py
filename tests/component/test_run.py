import unittest
from functools import partial
from unittest.mock import Mock
from run.run import Run

#Tests

class RunTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.run_draft = partial(MockRun,
            names='names', tags='tags', basedir='basedir', 
            file_pattern='file_pattern', recursively='recursively',
            existent='existent', stackless='dispatcher')
        
    def test_run(self):
        run = self.run_draft()
    
    
#Fixtures

class MockRun(Run):

    #Protected

    _dispatcher_class = Mock(return_value=Mock(add_handler=Mock()))
    _cluster_class = Mock(return_value=Mock())    
    _callback_handler_class = Mock()
    _initiated_task_signal_class = Mock()
    _initiated_var_signal_class = Mock()
    _completed_task_signal_class = Mock()
    _retrieved_var_signal_class = Mock()
    _default_basedir = 'basedir'
    _default_file_pattern = 'file_pattern'        
    _logging_module = Mock()    