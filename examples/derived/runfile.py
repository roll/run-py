from run import Module, NullTask, DerivedTask

class MainModule(Module):
    
    task = NullTask()
    
    derived = DerivedTask(
        task='task',
    )