from .task import Task 

class NullTask(Task):

    #Public

    def invoke(self, *args, **kwargs):
        pass