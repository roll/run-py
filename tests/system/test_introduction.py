from tests.system.test_examples import ExamplesTest

class IntroductionTest(ExamplesTest):
    
    #Public        
    
    __test__ = True
    
    def test_greet(self):
        result = self._execute('greet', messages=['Hi'])
        self.assertEqual(
            result, 
            'Type your greeting [Hello]: '
            'Hi World!\n')
        
    #Protected 
        
    @property
    def _filename(self):
        return 'introduction.py'