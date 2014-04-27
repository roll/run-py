from unittest import skip
from tests.system.test_examples import ExamplesTest

class IntroductionTest(ExamplesTest):
    
    #Public        
    
    __test__ = True
    
    @skip('Requires box >= 0.14')
    def test_greet(self):
        result = self._execute('greet', messages=['Hi'])
        self.assertEqual(
            result, 
            'Type your greeting [Hello]: '
            'Your choice is "Hi".\n'
            'We\'re ready.\n'
            'Hi World!\n'
            'OK. We\'re done.\n')
        
    #Protected 
        
    @property
    def _filename(self):
        return 'introduction.py'