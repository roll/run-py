import os
from copy import copy
from contextlib import contextmanager
from abc import ABCMeta, abstractmethod
from ..attribute import Attribute
from ..dependency import require, trigger
from .signal import InitiatedTaskSignal, SuccessedTaskSignal, FailedTaskSignal

class Task(Attribute, metaclass=ABCMeta):
    
    #Public
        
    def __meta_init__(self, module, *args, **kwargs):
        self._args = ()
        self._kwargs = {}
        self._meta_dependencies = []
        self._add_dependencies(kwargs.pop('depend', []))        
        self._add_dependencies(kwargs.pop('require', []), require)
        self._add_dependencies(kwargs.pop('trigger', []), trigger)
        super().__meta_init__(module, *args, **kwargs)
        
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs        
        
    def __get__(self, module, module_class=None):
        return self
    
    def __set__(self, module, value):
        if callable(value):
            self.invoke = value
        else:
            raise TypeError(
            'Attribute is task "{task}" and '
            'can be set only to callable value'.
            format(task=self))
    
    def __call__(self, *args, **kwargs):
        self._add_signal('initiated')
        try:
            self._resolve_dependencies()
            try:
                result = self.effective_invoke(*args, **kwargs)
            except Exception:
                self._resolve_dependencies(is_fail=True)
                raise
            self._resolve_dependencies(is_fail=False)
        except Exception:
            self._add_signal('failed')
            raise
        self._add_signal('successed')
        return result
    
    @property
    def meta_dependencies(self):
        return self._meta_dependencies
             
    def depend(self, dependency):
        """Add custom dependency."""
        dependency.bind(self)
        self._meta_dependencies.append(dependency)
           
    def require(self, task, *args, **kwargs):
        """Add require dependency."""
        dependency = require(task, *args, **kwargs)
        self.depend(dependency)
        
    def trigger(self, task, *args, **kwargs):
        """Add trigger dependency."""        
        dependency = trigger(task, *args, **kwargs)
        self.depend(dependency)
             
    def enable_dependency(self, task, category=None):
        for dependency in self._meta_dependencies:
            if not category or isinstance(dependency, category):
                dependency.enable(task)
        
    def disable_dependency(self, task, category=None):
        for dependency in self._meta_dependencies:
            if not category or isinstance(dependency, category):
                dependency.disable(task)
    
    def effective_invoke(self, *args, **kwargs):
        with self._effective_dir():
            return self.invoke(
                *self._effective_args(*args), 
                **self._effective_kwargs(**kwargs))
                                     
    @abstractmethod
    def invoke(self, *args, **kwargs):
        pass #pragma: no cover
    
    #Protected
    
    _initiated_signal_class = InitiatedTaskSignal
    _successed_signal_class = SuccessedTaskSignal
    _failed_signal_class = FailedTaskSignal 
    
    def _add_dependencies(self, container, category=None):
        for dependency in container:
            if category and not isinstance(dependency, category):
                dependency = category(dependency)
            self.depend(dependency)
                
    def _resolve_dependencies(self, is_fail=None):
        for dependency in self._meta_dependencies:
            dependency.resolve(is_fail=is_fail)
            
    def _add_signal(self, name):
        signal_class_attr = '_'+name+'_signal_class' 
        signal_class = getattr(self, signal_class_attr)
        signal = signal_class(self)
        self.meta_dispatcher.add_signal(signal)
     
    @contextmanager
    def _effective_dir(self):
        if self.meta_chdir:
            cwd = os.getcwd()
            os.chdir(self.meta_basedir)
            yield
            os.chdir(cwd)
        else:
            yield 
            
    def _effective_args(self, *args):
        eargs = self._args+args
        eargs = tuple(map(self._expand_arg, eargs))
        return eargs
     
    def _effective_kwargs(self, **kwargs):
        ekwargs = copy(self._kwargs)
        ekwargs.update(kwargs)
        for key, value in ekwargs.items():
            ekwargs[key] = self._expand_arg(value)
        return ekwargs
    
    def _expand_arg(self, value):
        result = value
        if isinstance(value, module):
            result = value.expand(self.meta_module)
        return result
    

class module:
    
    #Public
    
    def __init__(self):
        self._get = False
        self._attr = ''
        self._call = False
        self._args = ()
        self._kwargs = {}
        
    def __getattr__(self, name):
        self._get = True
        self._attr = '.'.join(filter(None, [self._attr, name]))
        return self
    
    def __call__(self, *args, **kwargs):
        self._call = True
        self._args = args
        self._kwargs = kwargs
        return self
        
    def expand(self, module):
        result = module
        if self._get:
            result = getattr(result, self._attr)
        if self._call:
            result = result(*self._args, **self._kwargs)
        return result           