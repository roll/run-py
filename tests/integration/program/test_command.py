import unittest
from box.functools import cachedproperty
from run.program.command import Command
from run.settings import settings

# TODO: remove unittest inheritance?
class CommandTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.argv = ['run']

    @cachedproperty
    def command(self):
        return Command(self.argv, config=settings.argparse)

    def test_task(self):
        self.assertEqual(self.command.task,
                         self.command.default_task)

    def test_args(self):
        self.assertEqual(self.command.args, [])

    def test_kwargs(self):
        self.assertEqual(self.command.kwargs, {})


class CommandTest_with_task_and_arguments(CommandTest):

    # Public

    def setUp(self):
        self.argv = ['run', 'task', 'arg1,True,kwarg1=1,', 'kwarg2=1.5']

    def test_task(self):
        self.assertEqual(self.command.task, 'task')

    def test_args(self):
        self.assertEqual(self.command.args, ['arg1', True])

    def test_kwargs(self):
        self.assertEqual(self.command.kwargs, {'kwarg1': 1, 'kwarg2': 1.5})


class CommandTest_with_list_flag(CommandTest):

    # Public

    def setUp(self):
        self.argv = ['run', 'task', '-l']

    def test_task(self):
        self.assertEqual(self.command.task, 'list')

    def test_args(self):
        self.assertEqual(self.command.args, ['task'])


class CommandTest_with_info_flag(CommandTest_with_list_flag):

    # Public

    def setUp(self):
        self.argv = ['run', 'task', '-i']

    def test_task(self):
        self.assertEqual(self.command.task, 'info')


class CommandTest_with_meta_flag(CommandTest_with_list_flag):

    # Public

    def setUp(self):
        self.argv = ['run', 'task', '-m']

    def test_task(self):
        self.assertEqual(self.command.task, 'meta')
