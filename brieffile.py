from brief import Brief, PackageContext, FileTemplate, FileTarget

class Brief(Brief):
       
    context = PackageContext()
    template = FileTemplate('package.tpl')
    target = FileTarget('package.py')