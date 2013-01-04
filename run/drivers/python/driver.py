import os
import subprocess
from lib31.decorators.cachedproperty import cachedproperty
from run.drivers.base.driver import BaseDriver

class PythonDriver(BaseDriver):
    
    DATA = {         
        'dir': 'data',
        'map': {
            'connector': ['connector', 'connector.py']
        }
    }    

    def process(self):
        return subprocess.call(['python', self._connector], 
                               env=self._environ)

    @cachedproperty
    def _environ(self):
        environ = os.environ.copy()
        environ['RUN_COMMAND'] = self._command.json
        return environ
    
    @cachedproperty
    def _connector(self):
        return os.path.join(os.path.dirname(__file__), 
                            self.DATA['dir'], 
                            *self.DATA['map']['connector'])