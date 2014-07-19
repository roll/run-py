import unittest
from unittest.mock import Mock
from run.cluster.meta import MetaConstraint

class MetaConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = MetaConstraint(['name1, name2'], ['tag1', 'tag2'])
        self.emitter = Mock()

    def test___call___not_skip(self):
        pass
