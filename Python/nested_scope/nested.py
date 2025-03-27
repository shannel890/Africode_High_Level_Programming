#this is a nested function example
def calculator(operation):
    def add(a ,b):
        return a + b
        """a and b are input integers"""
        """adds integers"""
    
    def subtract(a ,b):
        return a - b
        """subtracts integers"""
    
    def multiply(a ,b):
        return a * b
        """multiplys integers"""
    
    def divide(a ,b):
        return a / b
        """divides integers"""
    
    if operation == "addition":
        return add
    
    elif operation == "subtraction":
        return subtract
    
    elif operation == "multiplication":
        return multiply
    
    elif operation == "division":
        return divide
    else:
        return"Invalid operation"
        """prints invalid if the operation is unknown"""

operation = input('Enter the operation: ' ).strip()
"""this inquires the operation to be used"""
a = int(input('Enter the first number: '))
"""prompt for the first digit"""
b = int(input('Enter the second number: '))
"""prompt for the second digit"""

operation_function = calculator(operation)
if callable(operation_function):
    """calls the operation_function if the input is correct"""
    result = operation_function(a, b)
    print(f"Result of the {operation}: {result}")
    """prints the results if the input is correct"""
else:
    print(operation_function)




    
# results = calculator(operation=(""))
# print(results)
    
    
    
# result_add = calculator("add")(3,4)
# print(f"addition results:{result_add}")
    
        