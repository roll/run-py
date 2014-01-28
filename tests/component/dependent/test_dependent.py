import unittest
from unittest.mock import Mock, call
from run.dependent.dependent import DependentAttribute

class DependentAttributeTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.MockDependency = self._make_mock_dependency_class()
        self.MockAttribute = self._make_mock_attribute_class(self.MockDependency)

    def test_require_and_resolve_requirments(self):
        attribute = self.MockAttribute(
            require=['task1'], module=None)
        attribute.require(['task2', 'task2'])
        attribute.require(['task3'])
        attribute.require(['task3'], disable=True)
        attribute._resolve_requirements()
        attribute._resolve_requirements()
        self.MockDependency.call.assert_has_calls([
            call(attribute, task='task1'), 
            call(attribute, task='task2')])
    
    def test_trigger_and_resolve_triggers(self):
        attribute = self.MockAttribute(
            trigger=['task1'], module=None)
        attribute.trigger(['task2', 'task2'])
        attribute.trigger(['task3'])
        attribute.trigger(['task3'], disable=True)
        attribute._resolve_triggers()
        attribute._resolve_triggers()
        self.MockDependency.call.assert_has_calls([
            call(attribute, task='task1'), 
            call(attribute, task='task2'),
            call(attribute, task='task1'), 
            call(attribute, task='task2')])
        
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
    
    def _make_mock_attribute_class(self, mock_dependency_class):
        class MockAttribute(DependentAttribute):
            #Public
            __get__ = Mock()
            __set__ = Mock()
            #Protected
            @staticmethod
            def _dependency_class(task):
                return mock_dependency_class(task)
        return MockAttribute