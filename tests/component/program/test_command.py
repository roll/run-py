import unittest
from functools import partial
from run.program.command import Command, settings


class CommandTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.pCommand = partial(Command, config=settings.argparse)

    def test(self):
        self.command = self.pCommand(['run'])
        self.assertEqual(self.command.attribute, self.command.default_task)
        self.assertEqual(self.command.arguments, {'args': [], 'kwargs': {}})

    def test_with_task_and_arguments(self):
        self.command = self.pCommand(
            ['run', 'attribute', 'arg1,True,kwarg1=1,', 'kwarg2=1.5'])
        self.assertEqual(self.command.attribute, 'attribute')
        self.assertEqual(self.command.arguments,
            {'args': ['arg1', True], 'kwargs': {'kwarg1': 1, 'kwarg2': 1.5}})

    def test_with_with_list_flag(self):
        self.command = self.pCommand(['run', 'attribute', '-l'])
        self.assertEqual(self.command.attribute, 'list')
        self.assertEqual(self.command.arguments, {'args': ['attribute'], 'kwargs': {}})

    def test_with_with_info_flag(self):
        self.command = self.pCommand(['run', 'attribute', '-i'])
        self.assertEqual(self.command.attribute, 'info')
        self.assertEqual(self.command.arguments, {'args': ['attribute'], 'kwargs': {}})

    def test_with_with_meta_flag(self):
        self.command = self.pCommand(['run', 'attribute', '-m'])
        self.assertEqual(self.command.attribute, 'meta')
        self.assertEqual(self.command.arguments, {'args': ['attribute'], 'kwargs': {}})
