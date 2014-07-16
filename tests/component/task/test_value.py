import unittest
from run.task.value import ValueTask

class ValueTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.task = ValueTask('value', meta_module=None)

    def test___call__(self):
        self.assertEqual(self.task(), 'value')

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)
