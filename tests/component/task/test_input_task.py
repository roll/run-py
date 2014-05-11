import unittest
from functools import partial
from unittest.mock import patch
from run.task.input import InputTask

class InputTaskTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.ptask = partial(InputTask, meta_module=None)
    
    @patch('box.io.rich_input')
    def test___call__(self, rich_input):
        task = self.ptask()
        result = task(*self.args, **self.kwargs)
        self.assertEqual(result, rich_input.return_value)
        rich_input.assert_called_with(*self.args, **self.kwargs)    