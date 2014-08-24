import os
from run import (Module, SubprocessTask, DerivedVar, DescriptorVar, FindVar,
                 FunctionVar, InputVar, MethodVar, NullVar,
                 RenderVar, SubprocessVar)

class Module(Module):

    # Tasks

    subprocess_task = SubprocessTask(
        prefix='echo "Hello World!"',
    )

    # Vars

    derived = DerivedVar(
        task='subprocess_task',
    )

    descriptor = DescriptorVar(
        descriptor=property(lambda self: True),
        meta_docstring='Return True.',
    )

    find = FindVar(
        string='find',
        getfirst=True,
    )

    function = FunctionVar(
        function=os.path.abspath,
        path='path',
    )

    input = InputVar(
        prompt='Type here',
    )

    method = MethodVar(
        method=lambda self: 'Hello World!',
        meta_docstring='Return "Hello World!".',
    )

    null = NullVar(
        require=['subprocess_task'],
    )

    subprocess = SubprocessVar(
        prefix='echo "Hello World!"',
    )
