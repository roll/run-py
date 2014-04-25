from tests.system.test_tasks import BaseTasksTest

class VarsTest(BaseTasksTest):
    
    #Public
    
    __test__ = True
    
    def test_derived(self):
        result = self._execute('derived')
        self.assertEqual(result, 'Hello World!\nNone\n')
        
    def test_function(self):
        result = self._execute('function')
        self.assertRegex(result, '.*examples/path\n')        
        
    def test_list(self):
        result = self._execute('list')
        self.assertEqual(len(result.splitlines()), 15)        
        
    def test_subprocess(self):
        result = self._execute('subprocess')
        self.assertEqual(result, 'Hello World!\nNone\n')        
    
    #Protected
    
    @property
    def _filename(self):
        return 'vars.py'