import unittest
from functools import partial
from unittest.mock import Mock, patch, call
from run.library import command


class CommandModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Module = self._make_mock_module_class()
        self.pModule = partial(self.Module, meta_module=None)
        self.module = self.pModule({'command1': 'command1'})

    @patch.object(command, 'CommandTask')
    def test(self, CommandTask):
        self.module = self.pModule({'command1': 'command1'})
        self.assertEqual(self.module.command0, CommandTask.return_value)
        self.assertEqual(self.module.command1, CommandTask.return_value)
        # Check CommandTask calls
        CommandTask.assert_has_calls(
            [call('command0', meta_module=self.module),
             call('command1', meta_module=self.module)],
            any_order=True)

    def test_meta_docstring(self):
        self.assertTrue(self.module.meta_docstring)

    def test_meta_tasks(self):
        self.assertEqual(sorted(self.module.meta_tasks),
            ['command0', 'command1', 'info', 'list', 'meta'])

    def test_meta_tasks_without_mapping(self):
        self.module = self.pModule()
        self.assertEqual(sorted(self.module.meta_tasks),
            ['command0', 'info', 'list', 'meta'])

    # Protected

    def _make_mock_module_class(self):
        class MockModule(command.CommandModule):
            # Protected
            _default_mapping = {'command0': 'command0'}
        return MockModule


class CommandTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.process = Mock(wait=Mock(return_value=0))
        self.Popen = Mock(return_value=self.process)
        patch.object(command, 'Popen', self.Popen).start()
        self.task = command.CommandTask(meta_module=None)

    def test___call__(self):
        self.task('command')
        self.Popen.assert_called_with('command', shell=True)

    def test___call___when_returncode_is_not_zero(self):
        self.process.wait.return_value = 1
        self.assertRaises(RuntimeError, self.task)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)
