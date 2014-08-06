import unittest
from functools import partial
from unittest.mock import patch
from run.task.input import InputTask


class InputTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.ptask = partial(InputTask, meta_module=None)

    @patch('box.io.enhanced_input')
    def test___call__(self, enhanced_input):
        task = self.ptask()
        result = task(*self.args, **self.kwargs)
        self.assertEqual(result, enhanced_input.return_value)
        enhanced_input.assert_called_with(*self.args, **self.kwargs)
