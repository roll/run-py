class Property:
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self._require = kwargs.get('require', [])
        self._help = kwargs.get('help', None)

    def help(self):
        if self._help:
            print(self._help)