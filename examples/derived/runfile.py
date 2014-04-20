from run import Module, DerivedTask

class MainModule(Module):
    
    def task(self):
        print('Hello world!')
    
    derived = DerivedTask(
        task='task',
    )