class Computer:
    def process(self):
        pass
    
class Laptop(Computer):
    def process(self):
        print("I am running on laptop")
        
class PC(Computer):
    def process(self):
        print("I am runnig on PC")

class Programming:
    def work(self, com):
        print("Runnig codes")
        com.process()
        
com1 = PC()
prog = Programming()
prog.work(com1)