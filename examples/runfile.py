from run import Module

class MainModule(Module):
    
    #Tasks
    
    def hello(self, who='World'):
        print('Hello {who}!'. format(who=who))