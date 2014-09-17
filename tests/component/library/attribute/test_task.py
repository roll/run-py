import unittest
from importlib import import_module
component = import_module('run.library.attribute.task')


@unittest.skip
class AttributeTaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.task = component.AttributeTask('attribute', meta_module=None)
        self.task.meta_module.attribute = 'attribute'

    # Tests

    def test___call__(self):
        self.assertEqual(self.task(), 'attribute')

    def test_meta_docstring(self):
        self.assertTrue(self.task.meta_docstring)
