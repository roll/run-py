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
     
    #Protected 
        
    @property
    def _filename(self):
        return 'modules.py'