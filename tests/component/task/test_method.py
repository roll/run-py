import unittest
from unittest.mock import Mock
from run.task.method import MethodTask


class MethodTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.method = Mock()
        self.task = MethodTask(self.method, meta_module=None)

    def test___call__(self):
        result = self.task(*self.args, **self.kwargs)
        self.assertEqual(result, self.method.return_value)
        self.method.assert_called_with(
            self.task.meta_module, *self.args, **self.kwargs)

    def test_meta_signature(self):
        self.assertEqual(self.task.meta_signature, '(*args, **kwargs)')

