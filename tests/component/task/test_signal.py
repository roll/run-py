import unittest
from unittest.mock import Mock, patch
from importlib import import_module
component = import_module('run.task.signal')


class TaskSignalTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.settings = Mock()
        patch.object(component, 'settings', self.settings).start()
        self.task = Mock()
        self.signal = component.TaskSignal(self.task, event='event')

    # Tests

    def test_format(self):
        self.settings.events = {'event': 'event'}
        self.settings.styles = {'event': {'foreground': 'bright_green'}}
        self.assertEqual(self.signal.format(), 'event')

    def test_format_with_task_meta_colorless_is_false(self):
        self.task.meta_colorless = False
        self.settings.events = {'event': 'event'}
        self.settings.styles = {'event': {'foreground': 'bright_green'}}
        self.assertEqual(self.signal.format(), '\x1b[92mevent\x1b[m')

    def test_task(self):
        self.assertEqual(self.signal.task, self.task)

    def test_event(self):
        self.assertEqual(self.signal.event, 'event')
