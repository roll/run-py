import unittest
from unittest.mock import Mock
from run.frame.task.build import build


class build_Test(unittest.TestCase):

    # Public

    def test(self):
        prototype = Mock(__meta_build__=Mock(return_value='builded_prototype'))
        builded_prototype = build(prototype, 'module')
        self.assertEqual(builded_prototype, 'builded_prototype')
        prototype.__meta_build__.assert_called_with('module')
