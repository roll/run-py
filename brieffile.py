from brief import PackageBrief, FileInput, FileOutput

class Brief(PackageBrief):
       
    input = FileInput('package.in')
    output = FileOutput('package.py')
    
    package = 'runtool'