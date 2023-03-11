'''class testClass:
    def __init__(self):
        return "I am a constructor method!"
    def instance_method(self):
        return "I am an instance method!"
    @classmethod
    def class_method(cls):
        return "I am a classmethod!"
    @staticmethod
    def static_method():
        return "I am a staticmethod!"'''
from datetime import date

class Person:
    def __init__(obj, esm, sen):
        obj.name = esm
        obj.age = sen
    @classmethod
    def class_method(myclass, name, birthdate):
        return myclass(name, (date.today().year - birthdate))
    @staticmethod
    def is_adult(my_age):
        return my_age > 18
    
person1 = Person("ali", 17)
print(person1.name, person1.age)

person2 = Person.class_method("ali", 2005)
print(person2.name, person2.age)