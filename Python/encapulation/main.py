#Encapulation in Python

class BankAccount:
    def __init__(self,owner,initial_balance):
        self.owner = owner #public attribute
        self._balance = initial_balance #protected attribute
        self.__pin = "1245" #private attribute

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited:{amount}")
            return True
        else:
            print("Deposit amount must be positive and greater than 0.")
            return False

    def withdraw(self,amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdraw:{amount}")
            return True
        else:
            print("Withdraw amount must be positive and less than or equal to the balance.")
            return False
        
    def get_balance(self):
        return self._balance
    
    
    def verify_pin(self,attempted_pin):
        return self.__pin == attempted_pin
    
    def change_pin(self,new__pin):
        return self.__pin == new__pin
    

    
account = BankAccount("kirui",3000)
# account.owner = "shannel"
# account._balance = "50000"
# print(account.owner)
# print(account._balance)

# print(account._BankAccount__pin)  # This works, but should be avoided
# print(account.verify_pin("1245"))
account.change_pin("1111")
print(account.verify_pin("1245"))

        