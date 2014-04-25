from tests.system.test_examples import ExamplesTest

class ModulesTest(ExamplesTest):

    #Public
    
    __test__ = True   
    
    def test_auto_list(self):
        result = self._execute('auto.list')
        self.assertRegex(result, '.*auto.factorial\n.*')
        
    def test_auto_factorial(self):
        result = self._execute('auto.factorial 5')
        self.assertEqual(result, '120\n')
        
    def test_find_list(self):
        result = self._execute('find.list')
        self.assertEqual(
            result,
            'find.default\n'
            'find.derived\n' 
            'find.descriptor\n' 
            'find.find\n' 
            'find.function\n' 
            'find.info\n' 
            'find.input\n' 
            'find.list\n' 
            'find.meta\n' 
            'find.method\n' 
            'find.null\n'
            'find.render\n' 
            'find.subprocess\n' 
            'find.value\n')               
     
    #Protected 
        
    @property
    def _filename(self):
        return 'modules.py'