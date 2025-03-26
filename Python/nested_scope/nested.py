#this is a nested function example
def calculator(operation):
    def add(a ,b):
        return a + b
    
    def subtract(a ,b):
        return a - b
    
    def multiply(a ,b):
        return a * b
    
    def divide(a ,b):
        return a / b
    
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

operation = input('Enter the operation:' ).strip()
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

operation_function = calculator(operation)
if callable(operation_function):
    result = operation_function(a, b)
    print(f"Result of the {operation}: {result}")
else:
    print(operation_function)




    
# results = calculator(operation=(""))
# print(results)
    
    
    
# result_add = calculator("add")(3,4)
# print(f"addition results:{result_add}")
    
        