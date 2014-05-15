import unittest
from functools import partial
from unittest.mock import Mock, call
from run.run.run import Run

class RunTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockRun = self._make_mock_run_class()
        self.prun = partial(MockRun,
            names='names', 
            tags='tags', 
            file='file', 
            basedir='basedir',
            recursively='recursively',
            strict='strict',)
        
    def test_run(self):
        run = self.prun()
        args = ('arg1',)
        kwargs = {'kwarg1': 'kwarg1',}
        run.run('attribute', *args, **kwargs)
        for attr in run._cluster_class.return_value.attribute:
            if hasattr(attr, 'assert_called_with'):
                attr.assert_called_with(*args, **kwargs)
        run._print.assert_has_calls([
            call('result1'), 
            call('result2'),
            call('attr3')])
    
    def test__controller(self):
        run = self.prun()
        run._controller
        run._controller_class.assert_called_with(
            run._dispatcher_class.return_value, 
            run._stack_class.return_value)
        
    def test__cluster(self):
        run = self.prun()
        run._cluster
        run._cluster_class.assert_called_with(
            names='names', 
            tags='tags', 
            file='file', 
            basedir='basedir',
            recursively='recursively',
            strict='strict', 
            dispatcher=run._dispatcher_class.return_value)
        
    def test__cluster_with_default_file_and_basedir(self):
        run = self.prun(file=None, basedir=None)
        run._cluster
        run._cluster_class.assert_called_with(
            names='names', 
            tags='tags', 
            file='default_file', 
            basedir='default_basedir',
            recursively='recursively',
            strict='strict', 
            dispatcher=run._dispatcher_class.return_value)        
        
    def test__dispatcher(self):
        run = self.prun()
        run._dispatcher
        run._dispatcher_class.assert_called_with()
        
    def test__stack(self):
        run = self.prun()
        self.assertEqual(run._stack, 'stack')
        run._stack_class.assert_called_with()
        
    def test__stack_with_plain_is_true(self):
        run = self.prun(plain=True)
        self.assertEqual(run._stack, None)
        self.assertFalse(run._stack_class.called)                             
    
    #Protected
    
    def _make_mock_run_class(self):
        class MockRun(Run):
            #Public
            default_file = 'default_file'
            default_basedir = 'default_basedir'
            #Protected
            _print = Mock()
            _task_class = Mock
            _controller_class = Mock()
            _dispatcher_class = Mock(return_value=Mock(add_handler=Mock()))
            _cluster_class = Mock(return_value=Mock(attribute = [
                Mock(return_value='result1'), 
                Mock(return_value='result2'),
                'attr3']))
            _stack_class = Mock(return_value='stack')
        return MockRun