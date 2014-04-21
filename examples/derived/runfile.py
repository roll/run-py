from run import Module, DerivedTask

class MainModule(Module):
    
    def task(self):
        """Print "Hello world!"
        """
        print('Hello world!')
    
    derived = DerivedTask(
        task='task',
    )