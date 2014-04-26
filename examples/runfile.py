from run import Module, InputVar

class MainModule(Module):
    
    #Tasks
    
    def greet(self, person='World'):
        print('{greeting} {person}!'.format(
            greeting=self.greeting, 
            person=person))
        
    #Vars
    
    greeting = InputVar(
        prompt='Your greeting',
        default='Hello',
    )