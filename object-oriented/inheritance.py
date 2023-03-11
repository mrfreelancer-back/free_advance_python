class Father:
    def F_features(self):
        print("This feature belongs to father")
        
class Child(Father):
    def C_features(self):
        print("This feature belongs to child")
object = Child()
object.F_features()
object.C_features()