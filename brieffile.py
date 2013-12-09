from brief import FileInput, FileOutput
from packgram.manage import PythonPackgramBrief

class Brief(PythonPackgramBrief):

    #Public
    
    input = FileInput('setup.tpl')
    output = FileOutput('setup.py')
    
    name = 'runpack'