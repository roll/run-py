from run import Run

class Run(Run):
    
    def test(self):
        print('test')
        
        
if __name__ == '__main__':
    run = Run()
    run.respond()