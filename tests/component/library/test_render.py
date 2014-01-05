import unittest
from unittest.mock import Mock
from run.library.render import RenderTask, ModuleTemplate, ModuleContext

class RenderTaskTest(unittest.TestCase):

    #Public

    def test(self):
        pass
    

class ModuleTemplateTest(unittest.TestCase):    
    
    #Public
    
    def test_render(self):
        template = Mock(
            new_context = Mock(return_value='new_context'),
            root_render_func=Mock(return_value='root_render'),
            _concat_operator=Mock(return_value='result'))
        self.assertEqual(ModuleTemplate.render(template, 'context'), 'result')
        template.new_context.assert_called_with('context', shared=True)
        template.root_render_func.assert_called_with('new_context')
        template._concat_operator.assert_called_with('root_render')
        
    
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