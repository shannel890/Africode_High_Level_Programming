# class User:
#     def __init__(self,username,id=None,courses=None,grade=None):
#         self.username = username
#         self.id = id
#         self.courses = [x for x in courses] if courses else []
#         self.grade = grade
        

#     def get_username(self):
#         return self.username
    
#     def get_id(self):
#         return self.id
    
#     def get_courses(self):
#         return self.courses
    
#     @classmethod
#     def user_with_grade(cls,username,grade:int):
#         return cls(username,grade=grade)
    
# user1 = User("kirui","567483", courses=["python", "java"], grade=95)
# print(f"{user1.get_username()} is id:{user1.get_id()} and does {user1.get_courses()} with grade {user1.grade}")

# user1 = User.user_with_grade("kirui" ,95)
# print(f"{user1.get_username()} has grade:{user1.grade}")

# class bankaccount:
#     def __init__(self,balance):
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount

#     def get_balance(self):
#         return self.balance
    
# account = bankaccount(2900)
# account.deposit(300)
# print(account.get_balance())
# class User:
#     @staticmethod
#     def add_phone_number(username,phone_number):
#         return f"{username} has phone_number {phone_number}"
    
# user1 = User.add_phone_number("kirui","0706368540")
# print(user1)

# class Cat:
#     def speak(self):
#         return "Meow"
    
# class Dog:
#     def speak(self):
#         return "Bark"
    
# def animal_sound(animal):
#     print(animal.speak())
        
# cat = Cat()
# dog = Dog()
# animal_sound(cat)
# animal_sound(dog)

# class A:
#     def method(self):
#         return "Method from A"
    
# class B(A):
#     def method(self):
#         return "Method from B"

# class C(A):
#     def method(self):
#         return "Method from C"

# class D(B,C):
#     pass
# print(D.__mro__)

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 *self.radius * self.radius
    
circle = Circle(5)
print(circle.area())
        