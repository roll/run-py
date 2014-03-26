import unittest
from functools import partial
from unittest.mock import Mock, call
from run.task.task import Task

class TaskTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.MockTask = self._make_mock_task_class()
        self.partial_task = partial(self.MockTask, build=True)

    def test___get__(self):
        task = self.partial_task()
        self.assertEqual(task.__get__('module'), task)
        
    def test___set__(self):
        task = self.partial_task()        
        value = lambda: 'value'
        task.__set__('module', value)
        self.assertEqual(task.invoke, value)
        
    def test___set___not_callable(self):
        task = self.partial_task()         
        self.assertRaises(TypeError, task.__set__, 'module', 'value')        
        
    def test___call__(self):
        task = self.partial_task() 
        self.assertEqual(task.__call__(), 'value')
        task.invoke.assert_called_with()
        task._meta_initiated_signal_class.assert_called_with(task)
        task._meta_successed_signal_class.assert_called_with(task)
        task.meta_dispatcher.add_signal.assert_has_calls(
            [call('initiated_signal'), call('successed_signal')])     
        
    #Protected
    
    def _make_mock_task_class(self):
        class MockTask(Task):
            #Public
            invoke = Mock(return_value='value')
            meta_dispatcher = Mock(add_signal = Mock())
            #Protected
            _meta_initiated_signal_class = Mock(return_value='initiated_signal')
            _meta_successed_signal_class = Mock(return_value='successed_signal')        
        return MockTask   