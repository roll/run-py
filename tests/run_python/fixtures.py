import os

class Process(object):
     
    @property            
    def cwd(self):
        return os.getcwd()
    
    @cwd.setter
    def cwd(self, value):
        os.chdir(value)
        

process = Process()