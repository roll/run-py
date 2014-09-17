import unittest
from importlib import import_module
component = import_module('run.library.null.task')


class NullTaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.task = component.NullTask(meta_module=None)

    # Tests

    def test___call__(self):
        self.assertEqual(self.task(), None)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)
