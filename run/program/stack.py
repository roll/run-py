class Stack(list):

    #Public

    def __repr__(self):
        names = []
        if len(self) >= 1:
            previous = self[0]
            names.append(previous.meta_qualname)
            for attribute in self[1:]:
                current = attribute
                if current.meta_module == previous.meta_module:
                    names.append(current.meta_name)
                else:
                    names.append(current.meta_qualname) 
                previous = current
        return '/'.join(names)
    
    def push(self, attribute):
        self.append(attribute)     