import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.event')


class TaskEventTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.task = Mock()
        self.event = component.TaskEvent(self.task)

    # Tests

    def test_task(self):
        self.assertEqual(self.event.task, self.task)
