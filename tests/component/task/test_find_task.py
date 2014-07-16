import unittest
from functools import partial
from unittest.mock import patch
from run.task.find import FindTask

class FindTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.ptask = partial(FindTask, meta_module=None)

    @patch('box.findtools.find_strings')
    def test___call__(self, find_string):
        task = self.ptask()
        result = task(*self.args, **self.kwargs)
        self.assertEqual(result, find_string.return_value)
        find_string.assert_called_with(*self.args, **self.kwargs)

    def test___call___with_unsopported_mode(self):
        self.assertRaises(ValueError, self.ptask, mode='unsupported')
