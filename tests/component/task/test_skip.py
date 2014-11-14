import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.skip')


class skip_Test(unittest.TestCase):

    # Tests

    def test(self):
        task = Mock()
        self.assertEqual(component.skip(task), task)
        self.assertEqual(getattr(task, component.skip.MARKER), True)
