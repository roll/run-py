import unittest
from functools import partial
from unittest.mock import patch, call
from run.library.command import module


class CommandModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Module = self._make_mock_module_class()
        self.pModule = partial(self.Module, meta_module=None)
        self.module = self.pModule({'command1': 'command1'})

    @patch.object(module, 'CommandTask')
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
        class MockModule(module.CommandModule):
            # Protected
            _default_mapping = {'command0': 'command0'}
        return MockModule
