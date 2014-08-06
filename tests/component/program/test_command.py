import unittest
from functools import partial
from unittest.mock import patch
from run.program.command import Command, settings


class CommandTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.pCommand = partial(Command, config=settings.argparse)

    @patch.object(Command, 'default_task')
    def test(self, default_task):
        command = self.pCommand(['run'])
        self.assertEqual(command.task, default_task)
        self.assertEqual(command.arguments, [])
        self.assertEqual(command.args, [])
        self.assertEqual(command.kwargs, {})

    def test_task_args_kwargs(self):
        command = self.pCommand(['run', 'task', 'arg1,', 'kwarg1=kwarg1'])
        self.assertEqual(command.task, 'task')
        self.assertEqual(command.arguments, ['arg1,', 'kwarg1=kwarg1'])
        self.assertEqual(command.args, ['arg1'])
        self.assertEqual(command.kwargs, {'kwarg1': 'kwarg1'})

    def test_list(self):
        command = self.pCommand(['run', 'task', '-l'])
        self.assertEqual(command.task, 'list')
        self.assertEqual(command.args, ['task'])

    def test_meta(self):
        command = self.pCommand(['run', 'task', '-m'])
        self.assertEqual(command.task, 'meta')
        self.assertEqual(command.args, ['task'])

    def test_info(self):
        command = self.pCommand(['run', 'task', '-i'])
        self.assertEqual(command.task, 'info')
        self.assertEqual(command.args, ['task'])
