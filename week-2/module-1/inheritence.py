class Shop:
    def __init__(self):
        self.cart = []
        self.get_payment = []

    def add_products(self,product):
        self.cart.append(product)
        self.product=product

    def product_pay(self,payment):
        self.get_payment.append(payment)
        self.payment=payment

class inheritShop(Shop):
    def __init__(self):
        super().__init__()
        
            
get_shop = Shop()

get_shop.add_products("Shoes")
get_shop.add_products("Foog")
get_shop.add_products("Bag")

get_shop.product_pay(800)
get_shop.product_pay(500)
get_shop.product_pay(600)

for product in get_shop.cart:
    print("Product : ", product )
print()
for payment in get_shop.get_payment:
    print("Payment : ", payment )

get_inherit_shop = inheritShop()

get_inherit_shop.add_products("Shoes")
get_inherit_shop.add_products("Foog")
get_inherit_shop.add_products("Bag")

get_inherit_shop.product_pay(800)
get_inherit_shop.product_pay(500)
get_inherit_shop.product_pay(600)

print(get_inherit_shop.cart, get_inherit_shop.get_payment)
# inheritence

class First:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
class Second(First):
     def __init__(self, name, email,country):
         self.country = country
         super().__init__(name, email)

class Third(Second):
    def __init__(self, name, email, country, city):
        self.city=city
        super().__init__(name, email, country)
        
thirdClass = Third("Subrota", "subrota4@gmail.com","Bangladesh","Rajshahi")

print(thirdClass.name, thirdClass.email, thirdClass.country, thirdClass.city)

class SimpleClass:
    def myFunct(self, value):
        self.name = value 
        return self.name 
        
sic = SimpleClass()


print(sic.myFunct("Subrota"))