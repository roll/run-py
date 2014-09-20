class Stack(list):

    # Public

    def push(self, task):
        self.append(task)

    def format(self):
        names = []
        if len(self) >= 1:
            previous = self[0]
            name = previous.meta_format(attribute='meta_fullname')
            names.append(name)
            for task in self[1:]:
                current = task
                if current.meta_module == previous.meta_module:
                    name = current.meta_format(attribute='meta_name')
                    names.append(name)
                else:
                    name = current.meta_format(attribute='meta_qualname')
                    names.append(name)
                previous = current
        return '/'.join(filter(None, names))