import unittest
from functools import partial
from run.program.command import Command, settings

class CommandTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.pCommand = partial(Command, config=settings.argparse)

    def test(self):
        command = self.pCommand(['run', 'attribute', 'arg1,', 'kwarg1=kwarg1'])
        self.assertEqual(command.attribute, 'attribute')
        self.assertEqual(command.arguments, ['arg1,', 'kwarg1=kwarg1'])
        self.assertEqual(command.args, ['arg1'])
        self.assertEqual(command.kwargs, {'kwarg1': 'kwarg1'})
