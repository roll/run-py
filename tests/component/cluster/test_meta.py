import unittest
from unittest.mock import Mock
from run.cluster.meta import MetaConstraint

class MetaConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = MetaConstraint(['name1', 'name2'], ['tag1', 'tag2'])
        self.emitter = Mock()

    def test___call___not_skip(self):
        self.emitter.object.meta_name = 'name1'
        self.emitter.object.meta_tags = ['tag1', 'tag3']
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___skip_name_is_descriptor(self):
        self.emitter.object.meta_name = property(lambda self: self)
        self.emitter.object.meta_tags = ['tag1', 'tag3']
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___skip_name_does_not_match(self):
        self.emitter.object.meta_name = 'name3'
        self.emitter.object.meta_tags = ['tag1', 'tag3']
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___skip_tags_is_descriptor(self):
        self.emitter.object.meta_name = 'name1'
        self.emitter.object.meta_tags = property(lambda self: self)
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___skip_tags_do_not_match(self):
        self.emitter.object.meta_name = 'name1'
        self.emitter.object.meta_tags = ['tag3']
        self.constraint(self.emitter)
