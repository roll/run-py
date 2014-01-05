import unittest
from unittest.mock import Mock
from run.library.render import RenderTask, ModuleContext

class RenderTaskTest(unittest.TestCase):

    #Public

    def test(self):
        pass
    
    
class ModuleContextTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.module = Mock(key='value', spec=['key'])
        self.context = ModuleContext(self.module)
        
    def test___contains__(self):
        self.assertTrue('key' in self.context)
    
    def test___getitem__(self):
        self.assertEqual(self.context['key'], 'value')
    
    def test___getitem___key_error(self):
        self.assertRaises(KeyError, self.context.__getitem__, 'no_key')