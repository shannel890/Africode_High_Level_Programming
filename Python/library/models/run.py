# import math
# PI = math.pi
# print(PI)

# from math import pi
# print(pi)

# import time
# print("hello ,World!")
# time.sleep(5)
# print("this is awesome")

# def countdown(n):
#     if n == 0:
#         print("Done")
#         return
#     print(n)
#     countdown(n - 1)
# countdown(5)
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(1))

# def factorial_iterative(n):
#     result = 1
#     for i in range(1,n + 1):
#         result *= i 
#     return result
# print(factorial_iterative(5))
# import sys
# print(sys.getrecursionlimit())


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(8))