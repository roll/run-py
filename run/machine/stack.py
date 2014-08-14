class Stack(list):

    # Public

    def __repr__(self):
        names = []
        if len(self) >= 1:
            previous = self[0]
            names.append(previous.meta_format(previous.meta_fullname))
            for task in self[1:]:
                current = task
                if current.meta_module == previous.meta_module:
                    names.append(current.meta_format(current.meta_name))
                else:
                    names.append(current.meta_format(current.meta_qualname))
                previous = current
        return '/'.join(names)

    def push(self, task):
        self.append(task)
