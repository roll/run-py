import unittest
from unittest.mock import Mock, patch
from importlib import import_module
component = import_module('run.library.command.task')


class CommandTaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.process = Mock(wait=Mock(return_value=0))
        self.Popen = Mock(return_value=self.process)
        patch.object(component, 'Popen', self.Popen).start()
        self.task = component.CommandTask(meta_module=None)

    # Tests

    def test___call__(self):
        self.task('command')
        self.Popen.assert_called_with('command', shell=True)

    def test___call___when_returncode_is_not_zero(self):
        self.process.wait.return_value = 1
        self.assertRaises(RuntimeError, self.task)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)
