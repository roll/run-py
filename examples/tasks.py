import os
from run import (Module, DerivedTask, DescriptorTask, FindTask, FunctionTask,
                 InputTask, MethodTask, NullTask, SubprocessTask)


class TasksModule(Module):

    # Tasks

    derived = DerivedTask(
        task='subprocess',
    )

    descriptor = DescriptorTask(
        descriptor=property(lambda self: True),
        meta_docstring='Return True.',
    )

    find = FindTask(
        string='find',
        getfirst=True,
    )

    function = FunctionTask(
        function=os.path.abspath,
    )

    input = InputTask(
        prompt='Type here',
    )

    method = MethodTask(
        method=lambda self: 'Hello World!',
        meta_docstring='Return "Hello World!".',
    )

    null = NullTask(
        require=['subprocess'],
    )

    subprocess = SubprocessTask(
        prefix='echo "Hello World!"',
    )
