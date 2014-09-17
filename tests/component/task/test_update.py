import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.update')


class UpdateTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.update = component.Update('method', 'value')

    # Tests

    def test_apply(self):
        task = Mock()
        self.update.apply(task)
        task.method.assert_called_with('value')
