import unittest
from unittest.mock import Mock
from run.frame.task.signal import TaskSignal


class TaskSignalTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.task = Mock()
        self.signal = TaskSignal(self.task, event='event')

    def test_format(self):
        self.signal._events = {'event': 'event'}
        self.signal._styles = {'event': {'foreground': 'bright_green'}}
        self.assertEqual(self.signal.format(), 'event')

    def test_format_with_task_meta_plain_is_false(self):
        self.task.meta_plain = False
        self.signal._events = {'event': 'event'}
        self.signal._styles = {'event': {'foreground': 'bright_green'}}
        self.assertEqual(self.signal.format(), '\x1b[92mevent\x1b[m')

    def test_task(self):
        self.assertEqual(self.signal.task, self.task)

    def test_event(self):
        self.assertEqual(self.signal.event, 'event')
