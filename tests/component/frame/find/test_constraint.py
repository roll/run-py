import unittest
import inspect
from unittest.mock import Mock
from run.frame.find.constraint import Constraint


class ConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = Constraint(Mock,
            key='key1',
            tags=['tag1', 'tag2'])
        self.emitter = Mock()
        self.emitter.objself = Mock
        self.emitter.objself.meta_key = 'key1'
        self.emitter.objself.meta_tags = ['tag1', 'tag3']
        self.emitter.module = inspect.getmodule(self.emitter.objself)

    def test___call__not_skip(self):
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___skip_object_is_imported(self):
        self.emitter.module = 'other_module'
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___skip_object_is_not_type(self):
        self.emitter.objself = Mock()
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___skip_object_is_not_subclass(self):
        self.constraint = Constraint(Exception)
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___skip_key_does_not_match(self):
        self.emitter.objself.meta_key = 'key2'
        self.emitter.objself.meta_tags = ['tag1', 'tag3']
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___skip_tags_do_not_match(self):
        self.emitter.objself.meta_tags = ['tag3']
        self.constraint(self.emitter)
