import unittest
from functools import partial
from unittest.mock import Mock, call
from run.task.task import Task

class TaskTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.MockDependency = self._make_mock_dependency_class()
        self.MockTask = self._make_mock_task_class(self.MockDependency)
        self.partial_task = partial(self.MockTask, module=None)

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
        task._initiated_signal_class.assert_called_with(task)
        task._processed_signal_class.assert_called_with(task)
        task.meta_dispatcher.add_signal.assert_has_calls(
            [call('initiated_signal'), call('processed_signal')])
        
    def test_require_and_resolve_requirments(self):
        task = self.partial_task(require=['task1'])
        task.require(['task2', 'task2'])
        task.require(['task3'])
        task.require(['task3'], disable=True)
        task._resolve_requirements()
        task._resolve_requirements()
        self.MockDependency.call.assert_has_calls([
            call(task, task='task1'), 
            call(task, task='task2')])
    
    def test_trigger_and_resolve_triggers(self):
        task = self.partial_task(trigger=['task1'])
        task.trigger(['task2', 'task2'])
        task.trigger(['task3'])
        task.trigger(['task3'], disable=True)
        task._resolve_triggers()
        task._resolve_triggers()
        self.MockDependency.call.assert_has_calls([
            call(task, task='task1'), 
            call(task, task='task2'),
            call(task, task='task1'), 
            call(task, task='task2')])        
        
    #Protected
    
    def _make_mock_dependency_class(self):
        class MockDependency:
            #Public
            call = Mock()
            def __init__(self, task):
                self.task = task
                self.is_resolved = False
            def resolve(self, attribute):
                self.call(attribute, task=self.task)
                self.is_resolved = True                
            @property
            def name(self):
                return self.task
        return MockDependency
    
    def _make_mock_task_class(self, mock_dependency_class):
        class MockTask(Task):
            #Public
            invoke = Mock(return_value='value')
            meta_dispatcher = Mock(add_signal = Mock())
            #Protected
            _initiated_signal_class = Mock(return_value='initiated_signal')
            _processed_signal_class = Mock(return_value='processed_signal')
            @staticmethod            
            def _dependency_class(task):
                return mock_dependency_class(task)
        return MockTask   