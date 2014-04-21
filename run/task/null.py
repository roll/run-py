from .task import Task 

class NullTask(Task):

    #Public
    
    @property    
    def meta_docstring(self):
        return self._meta_params.get('docstring', 
            'Task does nothing but resolve its dependencies.')    

    def invoke(self, *args, **kwargs):
        pass