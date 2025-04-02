class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def start_engine(self):
        return "Engine started..."
    


class ElectricCar(Vehicle):
    def __init__(self, make, model, year,battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        return "The electric motor is humming..."
    
    def get_battery_info(self):
        return f"The electric car has a capacity of {self.battery_capacity} kwh ."
    
class Engine:
    def __init__(self,power):
        self.power = power

    def get_power(self):
        return f"This engine produces {self.power} horsepower"
    
class ElectricSystem:
    def __init__(self,voltage):
        self.voltage = voltage

    def get_voltage(self):
        return f"This system runs on {self.voltage} volts."
    # print("value of ",__name__)
        
    
        
