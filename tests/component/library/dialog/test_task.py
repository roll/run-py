import unittest
from functools import partial
from unittest.mock import patch
from run.library.dialog import task


class DialogTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.ptask = partial(task.DialogTask, meta_module=None)

    @patch.object(task, 'Dialog')
    def test___call__(self, Dialog):
        dialog = Dialog.return_value
        task = self.ptask(message='message')
        result = task(*self.args, **self.kwargs)
        self.assertEqual(result, dialog.message.return_value)
        dialog.message.assert_called_with(
            *self.args, message='message', **self.kwargs)
