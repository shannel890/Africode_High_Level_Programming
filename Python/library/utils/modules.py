print('The file running is', __name__)
def calculator(operation):
    def add(a ,b):
        return a + b
        
    
    def subtract(a ,b):
        return a - b
        
    
    def multiply(a ,b):
        return a * b
        
    
    def divide(a ,b):
        return a / b
        
    
    if operation == "add":
        return add
    
    elif operation == "subtract":
        return subtract
    
    elif operation == "multiply":
        return multiply
    
    elif operation == "divide":
        return divide
    else:
        return"Invalid operation"

# results = calculator('add')(3,4)
# print(f"The results is : {results}")

if __name__ == "__main__":
    results = calculator('add')(3,4)
    print(f"The results is : {results}")