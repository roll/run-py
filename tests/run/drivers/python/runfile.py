#Test imports
import subprocess
from fixtures import Process
subprocess, Process

def function_normal(a, b='default', *args, **kwargs):
    """
    docstring
    """
    print('function_normal: {a}, {b}'.format(a=a, b=b))
    
def function_empty():
    pass
        
def _hiden():
    pass

var = 'var'


class ClassToRun(object):
    
    def method(self):
        """
        docstring
        """
        print('method')
        
    def _hiden(self):
        pass
    
    var = 'var'