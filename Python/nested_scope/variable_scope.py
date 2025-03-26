x = 2
def my_name():
    global x 
    x = 5
    print(x)

my_name()
print(x)