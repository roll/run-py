import unittest
import inspect
from unittest.mock import Mock
from run.cluster.common import CommonConstraint

class CommonConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = CommonConstraint(Mock)
        self.emitter = Mock()
        self.emitter.object = Mock
        self.emitter.module = inspect.getmodule(self.emitter.object)

    def test___call__(self):
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___skip_object_is_imported(self):
        self.emitter.module = 'other_module'
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___skip_object_is_not_type(self):
        self.emitter.object = Mock()
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___skip_object_is_not_subclass(self):
        self.constraint = CommonConstraint(Exception)
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
