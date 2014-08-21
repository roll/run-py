class Stack(list):

    # Public

    def push(self, operation):
        self.append(operation)

    def format(self):
        names = []
        if len(self) >= 1:
            previous = self[0]
            names.append(previous.meta_format(mode='fullname'))
            for operation in self[1:]:
                current = operation
                if current.meta_module == previous.meta_module:
                    names.append(current.meta_format())
                else:
                    names.append(current.meta_format(mode='qualname'))
                previous = current
        return '/'.join(filter(None, names))