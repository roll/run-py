import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('run.task.build')


class build_Test(unittest.TestCase):

    # Tests

    def test(self):
        prototype = Mock(__meta_build__=Mock(return_value='builded_prototype'))
        builded_prototype = component.build(prototype, 'module')
        self.assertEqual(builded_prototype, 'builded_prototype')
        prototype.__meta_build__.assert_called_with('module')
