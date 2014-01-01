import unittest
from unittest.mock import Mock, call
from run.dependent.dependent import DependentAttribute

#Tests

class DependentAttributeTest(unittest.TestCase):

    #Public

    def test_require_and_resolve_requirments(self):
        attribute = MockDependentAttribute(require=['task1'], module=None)
        attribute.require(['task2', 'task2'])
        attribute.require(['task3'])
        attribute.require(['task3'], disable=True)
        attribute._resolve_requirements()
        attribute._resolve_requirements()
        MockTask.call.assert_has_calls([
            call(attribute, task='task1'), 
            call(attribute, task='task2')])
    
    def test_trigger_and_process_triggers(self):
        attribute = MockDependentAttribute(trigger=['task1'], module=None)
        attribute.trigger(['task2', 'task2'])
        attribute.trigger(['task3'])
        attribute.trigger(['task3'], disable=True)
        attribute._process_triggers()
        attribute._process_triggers()
        MockTask.call.assert_has_calls([
            call(attribute, task='task1'), 
            call(attribute, task='task2'),
            call(attribute, task='task1'), 
            call(attribute, task='task2')])        
    
    
#Fixtures

class MockTask:
    
    #Public
    
    call = Mock()
    
    def __call__(self, attribute):
        self.call(attribute, task=self.task)
        self.is_executed = True
    
    def __init__(self, task):
        self.task = task
        self.is_executed = False
        
    @property
    def name(self):
        return self.task
    

class MockDependentAttribute(DependentAttribute):
   
    #Public
    
    __get__ = Mock()
    __set__ = Mock()
    
    #Protected
    
    @staticmethod
    def _task_class(task):
        return MockTask(task)