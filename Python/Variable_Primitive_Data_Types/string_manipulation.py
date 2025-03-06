#******String slicing**************
#greeting = "Hello"
#name = "John Doe"
#x = greeting + " " + name
#print(x)

# x = greeting + " " + name[0:4]
# print(x)

#*********concatenation*********
# greeting = "Hello "
# name = "Jane Doe"

# x = "Hello " + name
# print(x)
#*********string methods***********
#name = "john doe"
#new_name = "DOE"

#1 capitalize() method*******
#cap_name = name.capitalize()
#print(cap_name)

#***********2 upper() method*****
#upper_name = name.upper()
#print(upper_name)

#******3 lower() method****
#lower_name = new_name.lower()
#print(lower_name)

#*********4 count() method******
#print(name.count('o'))
#phone = ["0726","456","783"]


#*****5 split **********

#new_list = name.split()
#print(new_list)
#new_phone = phone.split('-')
#print(new_phone)

#**********6 join() method

#joined_phone = "".join(phone)
#print(joined_phone)
#print(type(phone))
#print(type(joined_phone))

#*******7. isalnum()******
#python3 = "python3"
#print(python3.isalnum()) 


#print(python3.isalnum())
#*****8. isalpha()*******
#print(python3.isalpha())

#text = "python123"
#text2 = "0123"

#print(text.isdigit())

#********10. isspace() ********
#text = " "
#print(text.isspace())

#**********11. startswith()*****
#python = "python3"
#print(python.startswith("p"))

#**********12. endswith()*****
#python = "python3"
#print(python.endswith("n3"))

#********13. replace()******
#my_string = "I love python"
#new_string = my_string.replace("python", "javascript")
#print(new_string)

#**********14. f-string*****

text = "Python  "
print(text)
new_text = text.strip()
print(new_text)
   #old way of formatting strings
string = "John"
age = 23 
height = 5.76

#print("Hello, {} you are {} years old {} tall ".format(string, age, height))
 
         #f-string

#print(f"Hello, {string} you are {age} years old and {height} tall")