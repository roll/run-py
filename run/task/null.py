from .task import Task 

class NullTask(Task):

    #Public

    def complete(self, *args, **kwargs):
        pass