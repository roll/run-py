import unittest
from unittest.mock import Mock
from run.dependency.dependency import Dependency

class DependencyTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.attribute = Mock(meta_module=Mock(
            task1=Mock(), task2=Mock()))
        MockDependency = self._make_mock_dependency_class()
        self.tasks = ['task1', 'task2']
        self.dependency = MockDependency(self.tasks)
        
    def test___call__(self):
        function = 'function'
        decorated = self.dependency(function)
        self.assertIsInstance(decorated, self.dependency._builder_class)
        self.dependency._method_task_class.assert_called_with(function)
        self.dependency._add_dependency.assert_called_with(decorated)
        
    def test___call__with_method_is_builder(self):
        builder = self.dependency._method_task_class('method')
        decorated = self.dependency(builder)
        self.assertIs(decorated, builder)
        self.dependency._add_dependency.assert_called_with(decorated)
        
    def test_resolve(self):
        self.dependency.resolve(self.attribute)
        self.attribute.meta_module.task1.assert_called_with()
        self.attribute.meta_module.task2.assert_called_with()
        
    def test_is_resolved(self):
        self.assertEqual(self.dependency.is_resolved, False)          
        
    #Protected
    
    def _make_mock_dependency_class(self):
        class MockDependency(Dependency):
            #Public
            is_resolved = False
            #Protected
            _builder_class = Mock
            _method_task_class = Mock(return_value=Mock(
                require=Mock(), 
                trigger=Mock()))
            _add_dependency = Mock()
        return MockDependency
        
        
# class DependencyTest_with_args_and_kwargs(unittest.TestCase):
# 
#     #Public
#     
#     def setUp(self):
#         self.args = ('arg',)
#         self.kwargs = {'kwarg': 'kwarg'}
#         self.dependency = TaskDependency(
#             ('task', self.args, self.kwargs))
#         self.attribute = Mock(meta_module=Mock(task=Mock()))
#         
#     def test_resolve(self):
#         self.dependency.resolve(self.attribute)
#         self.attribute.meta_module.task.assert_called_with(
#             *self.args, **self.kwargs)
#         
#     def test_args(self):
#         self.assertEqual(self.dependency.args, ('arg',))
#         
#     def test_kwargs(self):
#         self.assertEqual(self.dependency.kwargs, {'kwarg': 'kwarg'})           