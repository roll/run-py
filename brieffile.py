from brief import FileInput, FileOutput
from briefbooks import PackageBrief

class Brief(PackageBrief):
       
    input = FileInput('package.in')
    output = FileOutput('package.py')
    
    package = 'runtool'