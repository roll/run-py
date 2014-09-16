import unittest
from functools import partial
from unittest.mock import patch
from run.library.render import task


class RenderTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.ptask = partial(task.RenderTask, meta_module=None)

    @patch.object(task.render, 'render_file')
    def test___call___with_mode_is_file(self, render_file):
        task = self.ptask(mode='file')
        result = task(*self.args, **self.kwargs)
        self.assertEqual(result, render_file.return_value)
        render_file.assert_called_with(
            *self.args, context=task.meta_module, **self.kwargs)

    def test___call___with_mode_is_unsopported(self):
        self.assertRaises(ValueError, self.ptask, mode='unsupported')
