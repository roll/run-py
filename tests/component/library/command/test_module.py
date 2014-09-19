import unittest
from functools import partial
from unittest.mock import patch
from importlib import import_module
component = import_module('run.library.command.module')


class CommandModuleTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.pModule = partial(component.CommandModule, meta_module=None)
        self.module = self.pModule({'command': 'command'})

    # Tests

    @patch.object(component, 'CommandTask')
    def test(self, CommandTask):
        self.module = self.pModule({'command': 'command'})
        self.assertEqual(self.module.command, CommandTask.return_value)
        # Check CommandTask calls
        CommandTask.assert_called_with('command', meta_module=self.module)

    def test_meta_docstring(self):
        self.assertTrue(self.module.meta_docstring)

    def test_meta_tasks(self):
        self.assertEqual(sorted(self.module.meta_tasks),
            ['command', 'info', 'list', 'meta'])
