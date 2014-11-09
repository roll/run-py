from .controller import Controller


class Runner:

    # Public

    def __init__(self, module, *, controller=None):
        if controller is None:
            controller = Controller()
        module.meta_listen(controller)
        self.module = module
        self.controller = controller

    def run(self, __attribute=None, *args, **kwargs):
        attribute = self.module
        if __attribute is not None:
            attribute = getattr(self.module, __attribute)
        if not callable(attribute):
            print(attribute)
            return
        result = attribute(*args, **kwargs)
        if result is None:
            return
        if not isinstance(result, list):
            print(result)
            return
        for element in result:
            if element is not None:
                print(result)
                return
