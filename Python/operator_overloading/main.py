class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
            return f'({self.x},{self.y})'
    
p1 = Point(2,3)
p2 = Point(4,5)
result = p1 + p2
print(result)

class Mouse:
     def __init__(self, y, z):
          self.y = y
          self.z = z

     def __mul__(self, multiply):
          return Mouse(self.y * multiply, self.z * multiply)
     
     def __str__(self):
          return f"({self.y},{self.z})"
     
p1 = Mouse(6,7)
p2 = p1 * 5
print(p2)

            

    

            
            