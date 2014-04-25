from tests.system.test_examples import ExamplesTest

class ModulesTest(ExamplesTest):

    #Public
    
    __test__ = True   
    
    def test_auto(self):
        result = self._execute('auto -l')
        self.assertEqual(
            result,
            'auto.default\n'
            'auto.find_files\n' 
            'auto.find_objects\n'
            'auto.find_strings\n' 
            'auto.info\n' 
            'auto.list\n' 
            'auto.meta\n')
     
    #Protected 
        
    @property
    def _filename(self):
        return 'modules.py'