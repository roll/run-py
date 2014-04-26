from tests.system.test_examples import ExamplesTest

class IntroductionTest(ExamplesTest):
    
    #Public        
    
    __test__ = True    
    
    def greet(self):
        result = self._execute('greet')
        self.assertEqual(result, 'Hi World!\n')
        
    #Protected 
        
    @property
    def _filename(self):
        return 'introduction.py'