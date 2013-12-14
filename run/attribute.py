class AttributeMixin:
    
    #Public
    
    def __init__(self, *args, **kwargs):
        self.__namespace = None
        super().__init__(*args, **kwargs)
    
    def __get__(self, namespace, namespace_class=None):
        if not self.__namespace:
            self.__namespace = namespace
        if self.__namespace != namespace:
            raise RuntimeError(
                'Element "{0}" is already bound to namespace "{1}"'.
                format(self, self.__namespace))
        return self

    @property
    def namespace(self):
        return self.__namespace
    
    
class DependentAttributeMixin(AttributeMixin):
    
    def __init__(self, *args, **kwargs):
        self.__require = kwargs.pop('require', [])
        super().__init__(*args, **kwargs)
        
    def resolve(self):
        for task_name in self.__require:
            task = getattr(self.namespace, task_name)
            task()    