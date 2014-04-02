import unittest
from unittest.mock import Mock
from run.task.nested import NestedTask

class NestedTaskTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.MockTask = self._make_mock_task_class()
        self.task = self.MockTask('task', meta_module=None)
        
    def test_invoke(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}        
        self.assertEqual(self.task.invoke(*self.args, **self.kwargs), 'value')
        self.task.meta_module.task.assert_called_with(*self.args, **self.kwargs)
        
    #Protected
    
    def _make_mock_task_class(self):
        class MockTask(NestedTask):
            #Public
            meta_module = Mock(task=Mock(return_value='value'))
        return MockTask