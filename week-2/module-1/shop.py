class Shop:
    def __init__(self):
        self.cart = []
        self.balance = 0
        
    def shopping(self, value):
        self.cart.append(value)
        
    def __repr__(self):
      try:
          self.balance+=120 
      finally:
          return " Amount added successfully !!"

    def add_balance(self, value):
     self.balance+=value
     
getCart = Shop()
getCart.shopping("Shoes")
getCart.shopping("Beg")
getCart.shopping("Neakless")
result = list(filter(lambda x:x != "Shoes", getCart.cart))
# getCart.cart.append(result)
print(result)
# print(getCart.cart)
# print(dir(getCart))
getCart.add_balance(899)
print(getCart.balance)