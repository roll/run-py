import unittest
from unittest.mock import Mock, patch
from run.task.task_function import task

class task_Test(unittest.TestCase):

    #Public

    def setUp(self):
        self.method = 'method'
        self.kwargs = {'kwarg1': 'kwarg1'}        
        self.task_class = Mock(return_value='task')
        patch.object(task, '_task_class', new=self.task_class).start()
        self.addCleanup(patch.stopall)

    def test_as_function(self):
        self.assertEqual(task(self.method, **self.kwargs), 'task')
        self.task_class.assert_called_with(self.method, **self.kwargs)
        
    def test_as_decorator(self):
        self.assertEqual(task(**self.kwargs)('method'), 'task')
        self.task_class.assert_called_with(self.method, **self.kwargs)        