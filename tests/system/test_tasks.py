from tests.system.test_examples import ExamplesTest

class BaseTasksTest(ExamplesTest):

    #Public
    
    __test__ = False    
    
    def test_default(self):
        result = self._execute('-f tasks.py')
        self.assertEqual(
            result,
            'default\n'
            'derived\n' 
            'descriptor\n' 
            'find\n' 
            'function\n' 
            'info\n' 
            'input\n' 
            'list\n' 
            'meta\n' 
            'method\n' 
            'null\n'
            'render\n' 
            'subprocess\n' 
            'value\n')
        
    def test_derived(self):
        result = self._execute('derived')
        self.assertEqual(result, 'Hello World!\n')
        
    def test_descriptor(self):
        result = self._execute('descriptor')
        self.assertEqual(result, 'True\n')
        
    def test_find(self):
        result = self._execute('find')
        self.assertEqual(result, 'find\n')
        
    def test_function(self):
        result = self._execute('function path')
        self.assertRegex(result, '.*examples/path\n')
        
    def test_info(self):
        result = self._execute('info default')
        self.assertRegex(result, 'default.*')
        
    def test_input(self):
        #TODO: implement
        pass
    
    def test_list(self):
        result = self._execute('list')
        self.assertEqual(len(result.splitlines()), 14)
        
    def test_meta(self):
        result = self._execute('meta default')
        self.assertRegex(result, ".*'type': 'NullTask'}\n")
        
    def test_method(self):
        result = self._execute('method')
        self.assertEqual(result, 'Hello World!\n')
        
    def test_null(self):
        result = self._execute('method')
        self.assertEqual(result, 'Hello World!\n')
        
    def test_render(self):
        result = self._execute('render')
        self.assertRegex(result, '.*RenderTask.*')
        
    def test_subprocess(self):
        result = self._execute('subprocess')
        self.assertEqual(result, 'Hello World!\n')
        
    def test_value(self):
        result = self._execute('value')
        self.assertEqual(result, 'value\n')
     
    #Protected 
        
    @property
    def _filename(self):
        return 'tasks.py'
    
    
class TasksTest(BaseTasksTest):

    #Public
    
    __test__ = True  