from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, bank_holder, balance):
        self.bank_holder = bank_holder #public
        self._balance = balance #protected
        
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self,amount):
     pass

class SavingAccount(BankAccount):
    def deposit(self, amount):
        if amount < 500 or amount >2500000:
            print("This amount is not supported !!")
        else:
            self._balance +=amount
            
    def withdraw(self, amount):
             if amount < 500 or amount >2500000:
              print("This amount is not supported !!")
             else:
              self._balance-=amount
              
              
saving = SavingAccount("Subrota", 5878)

saving.deposit(4581)
saving.withdraw(1455)

print(saving.bank_holder, saving._balance)

