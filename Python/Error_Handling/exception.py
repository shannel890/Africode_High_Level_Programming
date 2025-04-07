# from math import kirui
# print{"hello world"}
# a = 1
# b = 2
# def divide(a,b):
#     return a / b
# # results = divide(1/0)
# # print(results)
# try:
#     results = divide(1,0)
# except ZeroDivisionError as e:
#     print(f"Error:{e}")
# except TypeError as e:
#     print(f"Invalid input.Please enter a number")
# except:
#     print("An error has occurred")
# else:
#     print("Execution was successful!")
# finally:
#     print("I am being executed no matter what!")

#**********syntax error/complied*****  -Happens when you have written code that python does not understand 

# def func:
#     return None
# ************Indentation Error***********

# def func():
# return None

#******Exception Errors/Runtime*********** - Happens during execution of a program
# print("Hello" + int(5))

#Other exception errors
"""
-ValueError
-ZeroDivsionError
-KeyError
-IndexError
-FileNotFoundError
"""
#**NameError**
# print(kirui)

#*************Logical Error********
# def sum(a, b):
#     return a / b
# result = sum(10, 3)
# print(result)


#HANDLING MULTIPLE ERRORS
# try:
#     number = int(input("Enter a number:"))
#     results = 10 / number
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     print(results)
# finally:
#     print("Thanks for using our program")