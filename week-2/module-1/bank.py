
# print(balance)
class Bank :
    def __init__(self):
         self.balance=0
         
    def deposite(self, amount):
         if amount < 500 :
             print("Minimum deposit amount is 500 taka")
         else:
             self.balance+=amount 
        
    def withdraw(self, amount):
             if amount > 2500000 :
               print("Maximum withdraw amount is 2500000 taka")
             elif amount < 5000:
                 print("Minimum withdraw amount is 5000 taka")
             else:
              self.balance-=amount 
    def transfer(self, amount):
             if amount > 250000 :
               print("Maximum transfer amount is 2500000 taka")
             elif amount < 5000:
                 print("transfer withdraw amount is 5000 taka")
             else:
              self.balance-=amount 
              
bankInfo = Bank()

bankInfo.deposite(12000)

bankInfo.transfer(8000)
# print("="*10, end="")
print("="*10 ,"Your current Bank Balance is ", bankInfo.balance, " Taka ","="*10 )

