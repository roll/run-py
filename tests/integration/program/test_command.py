import unittest
from functools import partial
from run.program.command import Command
from run.settings import settings

class CommandTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.pCommand = partial(Command, config=settings.argparse)

    def test(self):
        self.command = self.pCommand(['run'])
        self.assertEqual(self.command.task, self.command.default_task)
        self.assertEqual(self.command.args, [])
        self.assertEqual(self.command.kwargs, {})

    def test_with_task_and_arguments(self):
        self.command = self.pCommand(
            ['run', 'task', 'arg1,True,kwarg1=1,', 'kwarg2=1.5'])
        self.assertEqual(self.command.task, 'task')
        self.assertEqual(self.command.args, ['arg1', True])
        self.assertEqual(self.command.kwargs, {'kwarg1': 1, 'kwarg2': 1.5})

    def test_with_with_list_flag(self):
        self.command = self.pCommand(['run', 'task', '-l'])
        self.assertEqual(self.command.task, 'list')
        self.assertEqual(self.command.args, ['task'])

    def test_with_with_info_flag(self):
        self.command = self.pCommand(['run', 'task', '-i'])
        self.assertEqual(self.command.task, 'info')
        self.assertEqual(self.command.args, ['task'])

    def test_with_with_meta_flag(self):
        self.command = self.pCommand(['run', 'task', '-m'])
        self.assertEqual(self.command.task, 'meta')
        self.assertEqual(self.command.args, ['task'])
