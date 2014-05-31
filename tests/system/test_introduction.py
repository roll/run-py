from tests.system.test_examples import ExamplesTest

class IntroductionTest(ExamplesTest):
    
    #Public        
    
    __test__ = True
    
    def test_greet(self):
        result = self._execute('greet', messages=['Hi'])
        self.assertEqual(
            result, 
            'Type your greeting (Hello): '
            'Your choice is "Hi".\n'
            'We\'re ready.\n'
            'Hi World!\n'
            'OK. We\'re done.\n')
        
    #Protected 
        
    @property
    def _file(self):
        return 'introduction.py'
