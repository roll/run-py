import types

class RunMeta(type):
   
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.iteritems():
            if isinstance(attr_value, types.FunctionType):
                attrs[attr_name] = cls.deco(attr_value)
        return type.__new__(cls, name, bases, attrs)


def require(*task_names):
    return