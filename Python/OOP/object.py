#Object Oriented Programming
# student = {
#     "name":"Kirui",
#     "age": 20,
#     "is_student": True,
#     "Courses":["math","science","history"],
#     "graduation_year":2025,
#     "GPA":3.9,
# }
# Attribute - properties of an object
# Method - functions that belong to an object

# Class - A blueprint for creating objects
class student:
    def __init__(self,name,age,id_number=None,courses=None):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.courses = [x for x in courses]if courses else[]

kirui = student("Shannel",19,id_number="894339",courses=["Python","HTML"])
kipla = student("Slayer",26,id_number="8940349",courses=["Python","JAVA"])
print(f"student name is {kirui.name} and age is {kirui.age} {kirui.courses}")
print(f"student name is {kipla.name} and age is {kipla.age} {kipla.id_number}")
# print(type(student))
    
