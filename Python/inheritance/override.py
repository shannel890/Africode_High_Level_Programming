from models import ElectricCar

my_tesla = ElectricCar("Tesla","Model S",2022,100)
print(my_tesla.get_info())
print(my_tesla.start_engine())
print(my_tesla.get_battery_info())