import types

class RunMeta(type):
   
    def __new__(cls, name, bases, classdict):
        for attr_name, attr_value in classdict.items():
            if isinstance(attr_value, types.FunctionType):
                classdict[attr_name] = cls.deco(attr_value)
        return type.__new__(cls, name, bases, classdict)


def require(*task_names):
    return