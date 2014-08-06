import unittest
from functools import partial
from unittest.mock import patch
from run.task.render import RenderTask


class RenderTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.ptask = partial(RenderTask, meta_module=None)

    @patch('box.jinja2.render_file')
    def test___call__(self, render_file):
        task = self.ptask()
        result = task(*self.args, **self.kwargs)
        self.assertEqual(result, render_file.return_value)
        render_file.assert_called_with(
            *self.args, context=task.meta_module, **self.kwargs)

    def test___call___with_unsopported_mode(self):
        self.assertRaises(ValueError, self.ptask, mode='unsupported')
