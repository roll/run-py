import unittest
from unittest.mock import Mock, patch
from run.task import signal


class TaskSignalTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.settings = Mock()
        patch.object(signal, 'settings', self.settings).start()
        self.task = Mock()
        self.signal = signal.TaskSignal(self.task, event='event')

    def test_format(self):
        self.settings.events = {'event': 'event'}
        self.settings.styles = {'event': {'foreground': 'bright_green'}}
        self.assertEqual(self.signal.format(), 'event')

    def test_format_with_task_meta_plain_is_false(self):
        self.task.meta_plain = False
        self.settings.events = {'event': 'event'}
        self.settings.styles = {'event': {'foreground': 'bright_green'}}
        self.assertEqual(self.signal.format(), '\x1b[92mevent\x1b[m')

    def test_task(self):
        self.assertEqual(self.signal.task, self.task)

    def test_event(self):
        self.assertEqual(self.signal.event, 'event')
