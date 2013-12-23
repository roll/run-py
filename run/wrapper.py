__all__ = ['Wrapper']

import inspect
import importlib

class Wrapper:
    
    #Public
    
    def wrap(self, obj):
        if callable(obj):
            return self.wrap_method(obj)
        elif inspect.isdatadescriptor(obj):
            return self.wrap_property(obj)
        else:
            return self.wrap_value(obj)
            
    def wrap_method(self, method):
        attr_class = self._import('task', 'MethodTask')
        return attr_class(method)
    
    def wrap_property(self, prop):
        attr_class = self._import('var', 'PropertyVar')
        return attr_class(prop)
    
    def wrap_value(self, value):
        attr_class = self._import('var', 'ValueVar')
        return attr_class(value)
       
    #Protected 
        
    @classmethod
    def _import(cls, module_name, attr_name):
        package_name = inspect.getmodule(cls).__package__
        module = importlib.import_module('.'+module_name, package_name)
        attr = getattr(module, attr_name)
        return attr         