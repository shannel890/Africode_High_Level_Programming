#Class Inheritance
#Parent Class
from models import Vehicle

#Child class
class Car(Vehicle):
    def __init__(self, make, model, year ,fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def get_fuel_type(self):
        return self.fuel_type
    
    def get_all_info(self):
        return f"{self.get_info()} - Fuel Type:{self.fuel_type}"
    
# print("value of ",__name__)
    
Car_1 = Car("Honda","Civic",2021,"Petrol")
if __name__ == "__main__":
    # print(Car_1.get_info())
    print(Car_1.get_all_info())


        