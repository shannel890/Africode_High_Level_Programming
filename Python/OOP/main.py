class User:
    def __init__(self,name,phone,is_admin ,is_logged_in=False):
        self.name = name
        self.phone = phone
        self.is_admin = is_admin
        self.is_logged_in = is_logged_in

    def user_role(self):
        if self.is_logged_in and self.is_admin:
            return "Dashboard"
        elif not self.is_logged_in:
            return "Login page"
        else:
            return "Newsfeed"
        
user1 = User("Ben","0765645342",is_logged_in=True,is_admin=False)
user2 = User("kipngeno","07894664743",is_logged_in=True,is_admin=True)
# print(f"{user1.name} redirected to {user1.user_role()}")
# print(f"{user2.name} redirected to {user2.user_role()}")

# def hello():
#     return "hello"
# print(type(hello))
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

# print(f"{p1.name} and {p1.age}")
class dog():
    def __init__(self,name):
        self.name = name
        

d = dog("tim")
print(d.name)
d2 = dog("bill")
# print(d2.name) 
        