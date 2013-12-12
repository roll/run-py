class RunMeta(type):
    
    #Public
    
    pass


class taskdecorator:
    
    #Public
    
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self._fget = fget
        self._fset = fset
        self._fdel = fdel
        self._doc = doc
               
    def __get__(self, obj, cls):
        if self._fget:
            cache = self._get_object_cache(obj)
            if self._name not in cache:
                cache[self._name] = self._fget(obj)
            return cache[self._name]
        else:
            raise AttributeError('Can\'t get attribute')

    def __set__(self, obj, value):
        if self._fset:
            self._fset(obj, value)
        else:
            raise AttributeError('Can\'t set attribute')
    
    def __delete__(self, obj):
        if self._fdel:
            self._fdel(obj)
        else:
            raise AttributeError('Can\'t delete attribute')
        
    @property
    def __doc__(self):
        if self._doc:
            return self._doc
        elif self._fget:
            return self._fget.__doc__
        else:
            return None               
    
    def getter(self, fget):
        self._fget = fget
        return self
      
    def setter(self, fset):
        self._fset = fset
        return self
    
    def deleter(self, fdel):
        self._fdel = fdel
        return self
    
    @classmethod
    def set(cls, obj, name, value):
        cache = cls._get_object_cache(obj)
        cache[name] = value
        
    @classmethod
    def reset(cls, obj, name):
        cache = cls._get_object_cache(obj)
        cache.pop(name, None)
            
    #Protected
    
    _object_cache_attribute_name = '_lib31_cached_properties'
    
    @property
    def _name(self):
        return self._fget.__name__
    
    @classmethod    
    def _get_object_cache(cls, obj):
        return obj.__dict__.setdefault(cls._object_cache_attribute_name, {})