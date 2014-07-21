import unittest
from functools import partial
from unittest.mock import patch
from run.program.command import Command, settings

class CommandTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.pCommand = partial(Command, config=settings.argparse)

    @patch.object(Command, 'default_attribute')
    def test(self, default_attribute):
        command = self.pCommand(['run'])
        self.assertEqual(command.attribute, default_attribute)
        self.assertEqual(command.arguments, [])
        self.assertEqual(command.args, [])
        self.assertEqual(command.kwargs, {})

    def test_attribute_args_kwargs(self):
        command = self.pCommand(['run', 'attribute', 'arg1,', 'kwarg1=kwarg1'])
        self.assertEqual(command.attribute, 'attribute')
        self.assertEqual(command.arguments, ['arg1,', 'kwarg1=kwarg1'])
        self.assertEqual(command.args, ['arg1'])
        self.assertEqual(command.kwargs, {'kwarg1': 'kwarg1'})

    def test_list(self):
        command = self.pCommand(['run', 'attribute', '-l'])
        self.assertEqual(command.attribute, 'list')
        self.assertEqual(command.args, ['attribute'])

    def test_meta(self):
        command = self.pCommand(['run', 'attribute', '-m'])
        self.assertEqual(command.attribute, 'meta')
        self.assertEqual(command.args, ['attribute'])

    def test_info(self):
        command = self.pCommand(['run', 'attribute', '-i'])
        self.assertEqual(command.attribute, 'info')
        self.assertEqual(command.args, ['attribute'])
