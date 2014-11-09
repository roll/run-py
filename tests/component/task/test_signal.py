import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.signal')


class TaskSignalTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.task = Mock()
        self.signal = component.TaskSignal(self.task)

    # Tests

    def test_task(self):
        self.assertEqual(self.signal.task, self.task)
