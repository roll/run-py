import unittest
from functools import partial
from unittest.mock import patch
from importlib import import_module
component = import_module('run.library.find.task')


class FindTaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.ptask = partial(component.FindTask, meta_module=None)

    # Tests

    @patch.object(component.find, 'find_strings')
    def test___call___with_mode_is_strings(self, find_string):
        task = self.ptask(mode='strings')
        result = task(*self.args, **self.kwargs)
        self.assertEqual(result, find_string.return_value)
        find_string.assert_called_with(*self.args, **self.kwargs)

    def test___call___with_mode_is_unsopported(self):
        self.assertRaises(ValueError, self.ptask, mode='unsupported')
