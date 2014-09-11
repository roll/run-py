import unittest
from functools import partial
from unittest.mock import patch
from run.library import prompt


class PromptTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.ptask = partial(prompt.PromptTask, meta_module=None)

    @patch.object(prompt, 'prompt')
    def test___call__(self, prompt):
        task = self.ptask()
        result = task(*self.args, **self.kwargs)
        self.assertEqual(result, prompt.return_value)
        prompt.assert_called_with(*self.args, **self.kwargs)


class PromptVarTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertTrue(issubclass(prompt.PromptVar, prompt.Var))
        self.assertTrue(issubclass(prompt.PromptVar, prompt.PromptTask))
