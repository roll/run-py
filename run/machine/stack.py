class Stack(list):

    # Public

    def push(self, task):
        self.append(task)

    def format(self):
        names = []
        if len(self) >= 1:
            previous = self[0]
            names.append(previous.meta_format(mode='fullname'))
            for task in self[1:]:
                current = task
                if current.meta_module == previous.meta_module:
                    names.append(current.meta_format())
                else:
                    names.append(current.meta_format(mode='qualname'))
                previous = current
        return '/'.join(names)