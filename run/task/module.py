class module:
    
    #Public
    
    def __init__(self):
        self._get = False
        self._attr = ''
        self._call = False
        self._args = ()
        self._kwargs = {}
        
    def __getattr__(self, name):
        self._get = True
        self._attr = '.'.join(filter(None, [self._attr, name]))
        return self
    
    def __call__(self, *args, **kwargs):
        self._call = True
        self._args = args
        self._kwargs = kwargs
        return self
        
    def expand(self, module):
        result = module
        if self._get:
            result = getattr(result, self._attr)
        if self._call:
            result = result(*self._args, **self._kwargs)
        return result