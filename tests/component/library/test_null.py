import unittest
from run.library.null import NullTask


class NullTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.task = NullTask(meta_module=None)

    def test___call__(self):
        self.assertEqual(self.task(), None)

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)
