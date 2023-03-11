print(len("Hamid")) # input as a string""
print(len([14, 85, 29, 996])) # input as a list[]

def sum(x, y, z=2):
    return x + y + z

print(f"The output of my sum: {sum(3, 4)}")

class Iran:
    def capital(self):
        print("Tehran is the capital of iran")
        
    def lang(self):
        print("Persian is the most spoken lang in iran")
        
    def type(self):
        print("Iran is an oskol country")
        
class Usa:
    def capital(self):
        print("Washington DC is the capital of usa")
        
    def lang(self):
        print("English is the most spoken lang in usa")
    
    def type(self):
        print("Usa is a developed country")
        
iran = Iran()
usa = Usa()

for country in [iran, usa]:
    country.capital()
    country.lang()
    country.type()

def run_polymorphics(obj):
    for country in obj:
        country.capital()
        country.lang()
        country.type()
    
iran = Iran()
usa = Usa()

run_polymorphics([iran, usa])

class Bird:
    def explain(self):
        print("There are too many types of birds")
        
    def flight(self):
        print("Most of the birds can fly but some can't")
        
class Sparrow(Bird):
    def flight(self):
        print("It can fly")
        
class Ostrich(Bird):
    def flight(self):
        print("It can't fly")

bird = Bird()
sprw = Sparrow()
ostrch = Ostrich()

bird.explain()
bird.flight()

sprw.explain()
sprw.flight()

ostrch.explain()
ostrch.flight()