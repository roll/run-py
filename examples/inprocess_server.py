from run import Run

class Run(Run):
    
    #Public
    
    def hello(self, person, times=1):
        """Prints 'Hello {person} {times} times!'"""
        print('Hello {person} {times} times!'.format(person=person,
                                                     times=str(times)))