class Stack(list):

    #Public

    def push(self, attribute):
        self.append(attribute)
        
    #TODO: rename?
    @property
    def formatted(self):
        names = []
        previous = self[0]
        names.append(previous.meta_qualname)
        for attribute in self[1:]:
            current = attribute
            if current.meta_module == previous.meta_module:
                names.append(current.meta_name)
            else:
                names.append(current.meta_qualname) 
            previous = current
        formatted = '/'.join(names)
        return formatted
            