#Polymorphism - comes from a greek word "polus" meaning many and "morphe" meaning forms
#It is a programming concept that allows objects of different 

#1.Method overriding
#2.Method overloading
#3.Operator overloading
#4.Duck typing

#1.Method overriding
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
    
#2.Method Overloading
class MathOperations:
    def add(self,a,b,c=0):
        return a + b + c
    
op1 = MathOperations()
print(op1.add(3,4))