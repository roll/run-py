from brief import FileInput, FileOutput
from briefbooks import PackageBrief

class Brief(PackageBrief):
    
    #Public
       
    input = FileInput('package.tpl')
    output = FileOutput('package.py')
    
    name = 'runpack'