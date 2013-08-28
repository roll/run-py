from brief import Brief, PackageContext, FileTemplate, FileTarget

class Brief(Brief):
    
    #TODO: add name = 'run-tool'
       
    context = PackageContext()
    template = FileTemplate('package.tpl')
    target = FileTarget('package.py')