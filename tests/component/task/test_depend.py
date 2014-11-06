import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.depend')


class depend_Test(unittest.TestCase):

    # Tests

    def test(self):
        dependency = Mock()
        method = Mock()
        result = component.depend(dependency)(method)
        self.assertEqual(result, dependency.return_value)
        # Check dependency call
        dependency.assert_called_with(method)
