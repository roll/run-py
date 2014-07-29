from .dependency import depend, require, trigger
from .module import (Module,
                     module, skip,
                     AutoModule, FindModule, NullModule, SubprocessModule)
from .settings import settings
from .task import (build, fork, task,
                   AttributeTask, DerivedTask, DescriptorTask, FindTask,
                   FunctionTask, InputTask, MethodTask, NullTask,
                   RenderTask, SubprocessTask)
from .var import (var,
                  AttributeVar, DerivedVar, DescriptorVar, FindVar,
                  FunctionVar, InputVar, MethodVar, NullVar,
                  RenderVar, SubprocessVar)
from .version import version
