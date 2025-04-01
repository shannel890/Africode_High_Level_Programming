# Methods - functions that belong to an object(defined inside a class)
class student:
    def __init__(self,name,age,scores=[],id_number=None,courses=None):
        self.name = name
        self.age = age
        self.scores = scores
        self.id_number = id_number
        self.courses = [x for x in courses]if courses else[]
    

    def pass_fail(self):
        if self.scores >= 50:
            return "Has passed"
        else:
            return "is a failure"
        
    def is_active(self):
        if self.courses == []:
            return "Not enrolled"
        else:
            return "Enrolled"
        
doro = student("Doro",20,50,"AASE09",courses=["python","java"] )
john = student(f"John",30,42, id_number="AASER04")

print(f"{doro.name} of ID {doro.id_number} {doro.pass_fail()} and {doro.is_active()}")
print(f"{john.name} of ID {john.id_number} {john.pass_fail()} and {john.is_active()}")
        

