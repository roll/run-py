import unittest
from run.task.attribute import AttributeTask


class AttributeTaskTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.task = AttributeTask('attribute', meta_module=None)
        self.task.meta_module.attribute = 'attribute'

    def test___call__(self):
        self.assertEqual(self.task(), 'attribute')

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)
