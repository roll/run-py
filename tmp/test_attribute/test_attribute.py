import unittest
from unittest.mock import Mock
from run.attribute.attribute import Attribute

class AttributeTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Module = self._make_mock_module_class()
        self.module = self.Module()
        self.Attribute = self._make_mock_attribute_class()
        self.attribute = self.Attribute(meta_module=None)

    def test(self):
        self.assertIsInstance(self.attribute, Attribute)

    def test___repr__(self):
        self.assertTrue(repr(self.attribute))

    def test___repr___if_meta_builded_is_false(self):
        self.attribute._meta_builded = False
        self.assertTrue(repr(self.attribute))

    def test_meta_dispatcher(self):
        self.assertEqual(self.attribute.meta_dispatcher,
                         self.attribute.meta_module.meta_dispatcher)

    def test_meta_dispatcher_setter(self):
        self.attribute.meta_dispatcher = 'dispatcher'
        self.assertEqual(self.attribute.meta_dispatcher, 'dispatcher')

    def test_meta_docstring(self):
        self.assertEqual(self.attribute.meta_docstring,
                         self.Attribute.__doc__)

    def test_meta_docstring_initter(self):
        self.attribute = self.Attribute(
            meta_module=None, meta_docstring='initter_docstring')
        self.assertEqual(self.attribute.meta_docstring, 'initter_docstring')

    def test_meta_docstring_setter(self):
        self.attribute.meta_docstring = 'setter_docstring'
        self.assertEqual(self.attribute.meta_docstring, 'setter_docstring')

    def test_meta_main_module(self):
        # NullModule
        self.assertFalse(self.attribute.meta_main_module)
        self.assertNotEqual(self.attribute.meta_main_module, None)

    def test_meta_module(self):
        # NullModule
        self.assertFalse(self.attribute.meta_module)
        self.assertNotEqual(self.attribute.meta_module, None)

    def test_meta_module_with_module(self):
        self.attribute = self.Attribute(meta_module=self.module)
        self.assertEqual(self.attribute.meta_module, self.module)

    def test_meta_name(self):
        self.assertEqual(self.attribute.meta_name, '')

    def test_meta_name_with_module(self):
        self.attribute = self.Attribute(meta_module=self.module)
        self.module.meta_attributes = {'attribute': self.attribute}
        self.assertEqual(self.attribute.meta_name, 'attribute')

    def test_meta_qualname(self):
        self.assertEqual(self.attribute.meta_qualname, '')

    def test_meta_qualname_with_module(self):
        self.attribute = self.Attribute(meta_module=self.module)
        self.module.meta_attributes = {'attribute': self.attribute}
        self.assertEqual(self.attribute.meta_qualname, 'module.attribute')

    def test_meta_qualname_with_module_is_main(self):
        self.attribute = self.Attribute(meta_module=self.module)
        self.module.meta_attributes = {'attribute': self.attribute}
        self.module.meta_is_main_module = True
        self.assertEqual(self.attribute.meta_qualname, '[module] attribute')

    def test_meta_type(self):
        self.assertEqual(self.attribute.meta_type, 'MockAttribute')

    # Protected

    def _make_mock_module_class(self):
        class MockModule:
            # Public
            meta_attributes = {}
            meta_basedir = 'basedir'
            meta_dispatcher = 'dispatcher'
            meta_is_main_module = False
            # Mocking NullModule
            meta_main_module = False
            meta_name = 'module'
            meta_qualname = 'module'
        return MockModule

    def _make_mock_attribute_class(self):
        class MockAttribute(Attribute):
            """docstring"""
            # Public
            __get__ = Mock()
            __set__ = Mock()
            __call__ = Mock()
        return MockAttribute
