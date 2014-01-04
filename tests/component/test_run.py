import unittest
from functools import partial
from unittest.mock import Mock, call
from run.run import Run

#Tests

class RunTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.run_draft = partial(MockRun,
            names='names', 
            tags='tags', 
            basedir='basedir',
            file_pattern='file_pattern', 
            recursively='recursively',
            existent='existent', 
            stackless='dispatcher')
        
    def test_run(self):
        run = self.run_draft()
        args = ('arg1',)
        kwargs = {'kwarg1': 'kwarg1'}
        run.run('attribute', *args, **kwargs)
        for attr in run._cluster_class.return_value.attribute:
            if hasattr(attr, 'assert_called_with'):
                attr.assert_called_with(*args, **kwargs)
        run._print_operator.assert_has_calls([
            call('result1'), 
            call('result2'),
            call('attr3')])
        
    def test__config(self):
        run = self.run_draft()
        run._callback_handler_class.assert_has_calls([
            call(run._on_initiated_attribute, signals=['itsc', 'ivsc']),
            call(run._on_executed_attribute, signals=['ctsc', 'rvsc'])])
        run._dispatcher_class.return_value.add_handler.assert_has_calls([
            call(run._callback_handler_class.return_value),
            call(run._callback_handler_class.return_value)])
        
    def test__dispatcher(self):
        run = self.run_draft()
        run._dispatcher
        run._dispatcher_class.assert_called_with()
        
    def test__cluster(self):
        run = self.run_draft()
        run._cluster
        run._cluster_class.assert_called_with(
            names='names', 
            tags='tags', 
            basedir='basedir',
            file_pattern='file_pattern', 
            recursively='recursively',
            existent='existent', 
            dispatcher=run._dispatcher_class.return_value)
        
    def test__basedir_default(self):
        run = self.run_draft(basedir=None)
        self.assertEqual(run._basedir, 'default_basedir')
        
    def test__file_pattern_default(self):
        run = self.run_draft(file_pattern=None)
        self.assertEqual(run._file_pattern, 'default_file_pattern')                            
    
    
#Fixtures  

class MockRun(Run):

    #Protected

    _print_operator = Mock()
    _task_class = Mock
    _dispatcher_class = Mock(return_value=Mock(add_handler=Mock()))
    _cluster_class = Mock(return_value=Mock(attribute = [
        Mock(return_value='result1'), 
        Mock(return_value='result2'),
        'attr3']))    
    _callback_handler_class = Mock(return_value=Mock())
    _initiated_task_signal_class = 'itsc'
    _initiated_var_signal_class = 'ivsc'
    _completed_task_signal_class = 'ctsc'
    _retrieved_var_signal_class = 'rvsc'
    _default_basedir = 'default_basedir'
    _default_file_pattern = 'default_file_pattern'        
    _logging_module = Mock()    