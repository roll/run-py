import unittest
from unittest.mock import Mock
from run.task.update import TaskUpdate

class TaskUpdateTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.update = TaskUpdate('method', 'value')

    def test_apply(self):
        task = Mock()
        self.update.apply(task)
        task.method.assert_called_with('value')
