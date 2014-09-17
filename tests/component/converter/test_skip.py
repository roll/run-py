import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.converter.skip')


class skip_Test(unittest.TestCase):

    # Public

    def test(self):
        task = Mock()
        self.assertEqual(component.skip(task), task)
        self.assertEqual(getattr(task, component.skip.attribute_name), True)
