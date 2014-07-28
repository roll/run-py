import unittest
from unittest.mock import Mock
from run.task.build import build

class build_Test(unittest.TestCase):

    # Public

    def test(self):
        prototype = Mock(__build__=Mock(return_value='builded_prototype'))
        builded_prototype = build(prototype, 'module')
        self.assertEqual(builded_prototype, 'builded_prototype')
        prototype.__build__.assert_called_with('module')
