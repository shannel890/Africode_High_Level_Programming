#Arbitrary args/kwargs
# def course_units(*args):
#     units = []
   
#     for unit in args:
#        units.append(unit)
#     print(units)
# course_units("HTML","CSS","JS","Python","Database","Flask")
# print(course_units)
# def student_info(**info):
#     for key,value in info.items():
#         print(f'{key}:{value}')
# print(student_info(name = "Enock",age = 20 ,course= "python",score=89))

# def performance_report(*args,**kwargs):
#     print(args)
#     print(kwargs)
# performance_report({'name' :'Kirui','age' : '19','score' : '90'},"HTML","CSS",status = "kip")
    
# def courses(*args):
#     print(args)
# courses("HTML","CSS","PTYHON","JS")
# def courses(*args):
#     print(args)
# courses("HTML","CSS","PTYHON","JS")

# def add_nums(*args):
#     return sum(args)

# print(add_nums(1,2,3,4))

# def details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# details(name = "kirui",age = 25, city= "nai")

def info(*args,**kwargs):
     print(args,kwargs)
     
    
# info({"name":"kirui"},name = "bob")

nums = [1,2,3,4]
details = {"name":"kirui","age":26}
info(*nums,**details)