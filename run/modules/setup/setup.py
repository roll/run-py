from subprocess import call
from ...task import Task

class SetupTask(Task):
    
    def test(self):
        "Test package"
        #TODO: check tests existing
        return call(['nosetests-3.3', 'tests', '-sv'])
     
    def build(self):
        "Build package"
        call(['python3.3', 'setup.py', 'sdist'])
        
    def register(self):
        "Upload package"
        call(['python3.3', 'setup.py', 'sdist', 'register', 'upload'])
          
    def clean(self):
        "Clean from dist, build, eggs"
        command = ' '.join(['rm', '-rfv', 'dist', 'build', '*.egg-info'])
        call(command, shell=True)
    
    def install(self):
        "Install package"
        self.build()
        command = ' '.join(['sudo', 'pip3', 'install', 'dist/*'])
        call(command, shell=True)

    def uninstall(self):
        "Uninstall package"
        call(['sudo', 'pip3', 'uninstall', '-y', self.name])