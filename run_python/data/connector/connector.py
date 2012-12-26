import os
import sys
import copy
import json
import types
import inspect
from abc import ABCMeta, abstractmethod
from lib31.decorators.cachedproperty import cachedproperty
from lib31.functions.load import load
 
def main():    
    connector = Connector(os.environ)
    connector.process()

         
class Connector(object):
    
    def __init__(self, environ):
        self._command = json.loads(environ['RUN_COMMAND'])
        
    def process(self):
        if not self._command['ishelp']:
            if self._command['function']:
                self._run()
            else:
                self._list()
        else:
            self._help()

    def _run(self):
        self._function(self._arguments)

    def _list(self):
        sys.stdout.write(self._functions.list)
    
    def _help(self):
        sys.stdout.write(self._function.help)  
    
    @cachedproperty
    def _function(self):
        try:
            return self._functions[self._command['function']]
        except KeyError:
            sys.stdout.write((
                'Function is not found\n'
                'Attempts: {functions}\n'
            ).format(
                functions=', '.join(sorted(self._functions))
            ))
            sys.exit(1)
    
    @cachedproperty
    def _functions(self):
        return Functions(self._command['runfile'],
                         self._command['runclass'])
       
    @cachedproperty
    def _arguments(self):
        return Arguments(self._command['arguments'])

 
class Functions(object):
    
    def __new__(cls, runfile, runclass):
        dirname = os.path.dirname(runfile)
        basename = os.path.basename(runfile).replace('.py', '')
        module = load(basename, path=[dirname])
        try:
            return ClassFunctions(getattr(module, runclass))
        except AttributeError:
            return ModuleFunctions(module)
    
    
class BaseFunctions(dict):
    
    __metaclass__ = ABCMeta

    @abstractmethod    
    def __init__(self):
        pass #pragma: no cover
    
    @cachedproperty
    def list(self):
        return '\n'.join(sorted(self))+'\n'
     
                
class ModuleFunctions(BaseFunctions):
        
    def __init__(self, module):
        functions = {}
        for name in dir(module):
            obj = getattr(module, name)
            if (not name.startswith('_') and
                isinstance(obj, types.FunctionType) and                
                getattr(obj, '__module__', None) == module.__name__):
                functions[name] = Function(obj)
        self.update(functions)


class ClassFunctions(BaseFunctions):
    
    def __init__(self, cls):
        functions = {}
        instance = cls()
        for name in dir(instance):
            obj = getattr(instance, name)
            if (not name.startswith('_') and
                isinstance(obj, (types.MethodType, 
                                 types.FunctionType,))):
                functions[name] = Function(obj)
        self.update(functions)


class Function(object):
    
    def __init__(self, function):
        self._function = function
        
    def __call__(self, arguments):
        return eval('self._function({arguments})'.
                    format(arguments=arguments), globals(), locals())

    @cachedproperty
    def help(self):
        return '\n'.join(self._signature+self._docstring)+'\n'

    @cachedproperty
    def _signature(self):
        return [('{name}({argstring})'.
                 format(name=self._name,
                        argstring=self._argstring))]
    
    @cachedproperty
    def _docstring(self):
        docstring = []
        getdoc = inspect.getdoc(self._function)
        if getdoc:
            docstring.append(getdoc)
        return docstring

    @cachedproperty
    def _name(self):
        return self._function.func_name

    @cachedproperty
    def _argstring(self):
        return ', '.join(self._argstring_general+
                         self._argstring_varargs+
                         self._argstring_keywords)

    @cachedproperty
    def _argstring_general(self):
        general = []
        defaults = copy.copy(self._defaults)
        for arg in reversed(self._args):
            if not defaults:
                general.insert(0, arg)
            else:
                default = repr(defaults.pop())
                general.insert(0, '{arg}={default}'.
                                  format(arg=arg, 
                                         default=default))
        return general
    
    @cachedproperty
    def _argstring_varargs(self):
        varargs = []
        if self._argspec.varargs:
            varargs.append('*{varargs}'.
                           format(varargs=self._argspec.varargs))
        return varargs
    
    @cachedproperty
    def _argstring_keywords(self):
        keywords = []
        if self._argspec.keywords:
            keywords.append('**{keywords}'.
                            format(keywords=self._argspec.keywords))
        return keywords

    @cachedproperty
    def _args(self):
        if self._ismethod:
            return self._argspec.args[1:]
        else:
            return self._argspec.args

    @cachedproperty
    def _defaults(self):
        if self._argspec.defaults:
            return list(self._argspec.defaults)
        else:
            return []

    @cachedproperty
    def _argspec(self):
        return inspect.getargspec(self._function)
    
    @cachedproperty
    def _ismethod(self):
        return isinstance(self._function, types.MethodType)


class Arguments(str):
    
    def __new__(cls, raw):
        arguments = []
        for argument in raw:
            (name, value,) = cls._split_argument(argument)            
            value = cls._represent_argument_value(value)
            arguments.append(cls._join_argument(name, value))            
        return str.__new__(cls, ', '.join(arguments))
    
    @staticmethod
    def _split_argument(argument):
        splited = argument.split('=', 1)
        argument = splited.pop()
        try:
            name = splited.pop()
        except IndexError:
            name = None
        return (name, argument)
    
    @staticmethod
    def _represent_argument_value(value):
        try:
            return str(eval(value, {}, {})) #TODO: pass len([]) etc - fix?
        except Exception:
            return repr(value)

    @staticmethod        
    def _join_argument(name, value):
        if not name:
            return value                
        else:
            return '='.join([name, value])

    
if __name__ == '__main__':
    main()           

import unittest

class ModuleFunctionsTest(unittest.TestCase):
    
    def setUp(self):
        self.runfile = ModuleFunctions(sys.modules[__name__])
        
    def test_list(self):
        self.assertEqual(self.runfile.list, 'main\n')


class FunctionTest(unittest.TestCase):
    
    def setUp(self):
        def function(a, b='default', *args, **kwargs): 
            """
            docstring
            """
            pass
        self.function = Function(function)
        
    def test_help(self):
        self.assertEqual(
            self.function.help, 
            "function(a, b='default', *args, **kwargs)\ndocstring\n"
        )

        
class FunctionTest_empty_function(unittest.TestCase):
    
    def setUp(self):
        def empty():
            pass
        self.function = Function(empty)
        
    def test_help(self):
        self.assertEqual(self.function.help, 'empty()\n')               