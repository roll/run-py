from run import Module, DerivedTask, DescriptorTask, FindTask, MethodTask

class MainModule(Module):
    
    #Tasks
    
    derived_task = DerivedTask(
        task='method_task',
    )
    
    @DescriptorTask
    @property
    def descriptor_task(self):
        """Return True
        """
        return True
        
    @MethodTask        
    def method_task(self):
        """Print "Hello world!"
        """
        print('Hello world!')
        
    find_task = FindTask(
        string='test',
    )