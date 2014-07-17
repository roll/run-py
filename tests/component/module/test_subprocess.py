import unittest
from unittest.mock import patch, call
from run.module import subprocess

class SubprocessModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.Task = patch.object(subprocess, 'SubprocessTask').start()
        self.Module = self._make_mock_module_class()
        self.module = self.Module({'command1': 'command1'},
            prefix='prefix_', separator='separator_', meta_module=None)

    def test(self):
        self.assertEqual(self.module.command0, self.Task.return_value)
        self.assertEqual(self.module.command1, self.Task.return_value)
        self.Task.assert_has_calls(
            [call(prefix='prefix_separator_command0',
                  separator='separator_',
                  meta_module=self.module),
             call(prefix='prefix_separator_command1',
                  separator='separator_',
                  meta_module=self.module)],
            any_order=True)

    def test_meta_docstring(self):
        self.assertTrue(self.module.meta_docstring)

    # Protected

    def _make_mock_module_class(self):
        class MockModule(subprocess.SubprocessModule):
            # Protected
            _default_mapping = {'command0': 'command0'}
        return MockModule
