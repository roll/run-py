import unittest
from unittest.mock import Mock, mock_open
from run.modules.render import RenderFileTask, ModuleTemplate, ModuleContext

class RenderFileTaskTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.template = Mock(render=Mock(return_value='text'))
        MockRenderFileTask = self._make_mock_render_file_task_class(self.template)
        self.source = '/source'
        self.target = '/target'
        self.task = MockRenderFileTask(module=None)
        
    def test_complete(self):
        self.task.complete(self.source, self.target)
        self.task._open_operator.assert_called_with(self.target, 'w')
        self.task._open_operator().write.assert_called_with('text')
        
    def test__get_template(self):
        self.assertEqual(self.task._get_template(self.source), self.template)
        self.task._file_system_loader_class.assert_called_with('/')
        self.task._environment_class.assert_called_with(loader='loader')
        self.assertEqual(
            self.task._environment_class.return_value.template_class,
            self.task._module_template_class)
        (self.task._environment_class.return_value.get_template.
            assert_called_with('source'))
        
    def test__get_context(self):
        self.assertEqual(self.task._get_context(), 'context')
        self.task._module_context_class.assert_called_with('module')        
    
    #Protected
    
    def _make_mock_render_file_task_class(self, template):
        class MockRenderFileTask(RenderFileTask):
            #Public
            meta_module = 'module'
            #Protected
            _environment_class = Mock(return_value=Mock(
                get_template=Mock(return_value=template)))
            _file_system_loader_class = Mock(return_value='loader')
            _module_template_class = Mock()
            _module_context_class = Mock(return_value='context')
            _open_operator = mock_open()
        return MockRenderFileTask
    

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