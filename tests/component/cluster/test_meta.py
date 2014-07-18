import unittest
from unittest.mock import Mock
from run.cluster.meta import MetaConstraint

class MetaConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = MetaConstraint(Mock)

    def test___call__(self):
        pass
