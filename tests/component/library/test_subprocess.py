import unittest
from functools import partial
from unittest.mock import Mock, patch, call
from run.library import subprocess


class SubprocessModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Module = self._make_mock_module_class()
        self.pModule = partial(
            self.Module,
            prefix='prefix_',
            separator='separator_',
            meta_module=None)
        self.module = self.pModule({'command1': 'command1'})

    @patch.object(subprocess, 'SubprocessTask')
    def test(self, SubprocessTask):
        self.module = self.pModule({'command1': 'command1'})
        self.assertEqual(self.module.command0, SubprocessTask.return_value)
        self.assertEqual(self.module.command1, SubprocessTask.return_value)
        # Check SubprocessTask calls
        SubprocessTask.assert_has_calls(
            [call(prefix='prefix_separator_command0',
                  separator='separator_',
                  meta_module=self.module),
             call(prefix='prefix_separator_command1',
                  separator='separator_',
                  meta_module=self.module)],
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
        class MockModule(subprocess.SubprocessModule):
            # Protected
            _default_mapping = {'command0': 'command0'}
        return MockModule


class SubprocessTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.task = subprocess.SubprocessTask(meta_module=None)
        self.process = Mock(wait=Mock(return_value=0))
        self.Popen = Mock(return_value=self.process)
        patch('subprocess.Popen', self.Popen).start()
        self.addCleanup(patch.stopall)

    def test___call__(self):
        self.task('command')
        self.Popen.assert_called_with('command', shell=True)

    def test___call___with_prefix_and_separator(self):
        self.task('command', prefix='prefix', separator='_')
        self.Popen.assert_called_with('prefix_command', shell=True)

    def test___call___when_returncode_is_not_zero(self):
        self.process.wait.return_value = 1
        self.assertRaises(RuntimeError, self.task)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)


class SubprocessVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(
            issubclass(subprocess.SubprocessVar, subprocess.Var))
        self.assertTrue(
            issubclass(subprocess.SubprocessVar, subprocess.SubprocessTask))
