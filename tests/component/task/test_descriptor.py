import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.descriptor')


class DescriptorTaskTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.descriptor = Mock(__get__=Mock(), __doc__='__doc__')
        self.task = component.DescriptorTask(self.descriptor, meta_module=None)

    # Tests

    def test___call__(self):
        result = self.task()
        self.assertEqual(result, self.descriptor.__get__.return_value)
        self.descriptor.__get__.assert_called_with(
            self.task.meta_module, type(self.task.meta_module))

    def test_meta_docstring(self):
        self.assertEqual(self.task.meta_docstring, self.descriptor.__doc__)
