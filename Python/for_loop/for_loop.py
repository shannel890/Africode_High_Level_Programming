#  Range (start,stop,step)
# for i in range(1,11,2):
#     print(i)   
# 
# LISTS
students = ["Dorothy","Rop","Kirui","Enock","Kipngeno"]
# for student in students:
#     print(student)    

# SETS
# students = set(students)
# for student in students:
#     print(student)
#print(type(students))


# *************Task**************
# 1. student1
# 2. student2
# 3. student3
# 4. student4

# Method 1 :Adding another variable
# count = 1
# for student in students:
#     print(count,student)
#     count += 1

# Method 2: Using len() and range()
# for t in range(len(students)):
#     print(t ,students[t])

# *******We cannot use the above method in iterating through objects in sets ******************
# sets_students = set(students)
# for index in range(len(sets_students)):
#     print(index,sets_students[index])

#Method 3:using enumerate()

# (a)List
# for i,student in enumerate(students):
    
#     print(i+1,student)

#pass
# for student in students:
#     pass
# for i in range(5):
#     print(i)

# for student in students:
#     if student == 'Kipngeno':
#         continue
#     print(student)

# else:
#     print('The list ends here')

# n = 0
# for n in range(1,7):
#     b = 0
#     for b in range(1,7):
       
#         print('_______')
#         print(f'{n} x {b} = {n*b}')
# def f(n):
#     if n == 0:
#         return 1
#     return n * f(n - 1)

# print(f(5))

# def t(a: int, b: int) -> int:
#     return a + b
# result = (3 + 5)
# print(result)  # Output: 8


