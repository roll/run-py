import unittest
from unittest.mock import patch
from importlib import import_module
component = import_module('run.program')


@unittest.skip
class ProgramTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.program = component.Program('argv')

    # Tests

    @unittest.skip
    @patch.object(component, 'Machine')
    def test___call__(self, Machine):
        self.program()
        # Check Machine call
        Machine.assert_called_with(
            filepath='filepath',
            compact='compact',
            plain='plain')
        # Check Machine's return value call
        Machine.return_value.run.assert_called_with(
            self.program._command.attribute,
            *self.program._command.arguments['args'],
            **self.program._command.arguments['kwargs'])

    def test_with_no_tasks(self):
        self.program = component.Program(['run'])
        self.assertEqual(self.program.attribute, None)
        self.assertEqual(self.program.arguments, {'args': [], 'kwargs': {}})

    def test_with_task_and_arguments(self):
        self.program = component.Program(
            ['run', 'attribute', 'arg1,True,kwarg1=1,', 'kwarg2=1.5'])
        self.assertEqual(self.program.attribute, 'attribute')
        self.assertEqual(
            self.program.arguments,
            {'args': ['arg1', True], 'kwargs': {'kwarg1': 1, 'kwarg2': 1.5}})

    def test_with_with_list_flag(self):
        self.program = component.Program(['run', 'attribute', '-l'])
        self.assertEqual(self.program.attribute, 'list')
        self.assertEqual(
            self.program.arguments,
            {'args': ['attribute'], 'kwargs': {}})

    def test_with_with_info_flag(self):
        self.program = component.Program(['run', 'attribute', '-i'])
        self.assertEqual(self.program.attribute, 'info')
        self.assertEqual(
            self.program.arguments,
            {'args': ['attribute'], 'kwargs': {}})

    def test_with_with_meta_flag(self):
        self.program = component.Program(['run', 'attribute', '-m'])
        self.assertEqual(self.program.attribute, 'meta')
        self.assertEqual(
            self.program.arguments,
            {'args': ['attribute'], 'kwargs': {}})
