
import datetime
import random

# --------------------------- Admin code start from here ---------------------------------

class Add_Item:
    def __init__(self, item_id, item_name, item_price, item_quantity):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def __repr__(self):
        return (f"Item ID: {self.item_id}\n"
                f"Item Name: {self.item_name}\n"
                f"Item Price: {self.item_price} taka\n"
                f"Item Quantity: {self.item_quantity}")


class Add_Customer:
    def __init__(self, customer_id, name, email, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address

    def __repr__(self):
        return (f"ID: {self.customer_id}\n"
                f"Name: {self.name.upper()}\n"
                f"Email: {self.email}\n"
                f"Address: {self.address}")


class Create_Admin_Account:
    def __init__(self, admin_id, name, email, address):
        self.admin_id = admin_id
        self.name = name
        self.email = email
        self.address = address

    def __repr__(self):
        return (f"ID: {self.admin_id}\n"
                f"Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Address: {self.address}")


class Admin:
    menu_list = []
    customer_list = []
    admin_list = []

    @classmethod
    def add_new_admin(self, admin_id, name, email, address):
        new_admin = Create_Admin_Account(admin_id, name, email, address)
        self.admin_list.append(new_admin)
        print("\n------- Account created successfully!! ---------\n")

    @classmethod
    def create_account(self):
        admin_id = random.randint(1, 205)
        name = input(">>> Enter your full name: ").lower()
        email = input(">>> Enter your valid email: ").lower()
        address = input(">>> Enter your current address: ")

        if any(admin.email == email for admin in self.admin_list):
            print("\n >>> This email is already used. Try another email. <<< \n")
        else:
            self.add_new_admin(admin_id, name, email, address)

    @classmethod
    def add_item(self, item_id, item_name, item_price, item_quantity):
        new_item = Add_Item(item_id, item_name, item_price, item_quantity)
        self.menu_list.append(new_item)
        print("\n --------- Your item added successfully ----------")

    @classmethod
    def remove_item(self, item_id):
        for item in self.menu_list:
            if item.item_id == item_id:
                self.menu_list.remove(item)
                print(f"\n >>> Item {item.item_name} has been removed from the menu!")
                return
        print("\n >>> Item not found with the given ID. <<< \n >>> Choose 6 to see your item ID <<< ")

    @classmethod
    def add_new_customer(self, customer_id, name, email, address):
        new_customer = Add_Customer(customer_id, name, email, address)
        self.customer_list.append(new_customer)
        print("\n ------- Customer account added successfully!! ---------")

    @classmethod
    def add_customer(self):
        customer_id = random.randint(1, 700)
        name = input(">>> Enter customer name: ").lower()
        email = input(">>> Enter customer email: ").lower()
        address = input(">>> Enter customer address: ")

        if any(customer.email == email for customer in self.customer_list):
            print("\n >>> This email is already used. Try another email. <<< \n")
        else:
            self.add_new_customer(customer_id, name, email, address)

    @classmethod
    def show_customers(self):
        if self.customer_list:
            print("\n >>> Customer List: \n")
            for customer in self.customer_list:
                print(customer)
                print()
        else:
            print("\n >>>>> No customers available.")

    @classmethod
    def remove_customer(self, customer_id):
        for customer in self.customer_list:
            if customer.customer_id == customer_id:
                self.customer_list.remove(customer)
                print(f"\n >>> Customer {customer.name} has been removed.")
                return
        print("\n >>> Customer not found with the given ID. \n >>> Choose 4 to see your customer ID")

    @classmethod
    def show_menu(self):
        if self.menu_list:
            print("\n >>> Menu of Items: \n")
            for item in self.menu_list:
                print(item)
                print()
        else:
            print("\n >>> No items in the menu.")

    @classmethod
    def set_item_price(self, item_id, item_price):
        for item in self.menu_list:
            if item.item_id == item_id:
                item.item_price = item_price
                print(f"\n >>> Item {item.item_name} price updated successfully!")
                return
        print("\n >>> Item not found with the given ID.\n >>> Choose 6 to get your item ID")

    @classmethod
    def admin_menu(self):
        while True:
            print("\n >>-------->> Welcome Dear Admin <<-----------<<\n")
            print("1. Add an item to the menu")
            print("2. Remove an item from the menu")
            print("3. Add a new customer")
            print("4. View all customer accounts")
            print("5. Remove a customer")
            print("6. Show menu")
            print("7. Update an item price")
            print("8. Exit from admin menu\n")

            try:
                choice = int(input(">>> Enter your choice: "))

                if choice == 1:
                    item_id = random.randint(1, 564)
                    item_name = input(">>> Enter item name: ").upper()
                    item_price = int(input(">>> Enter item price in BDT: "))
                    item_quantity = int(input(">>> Enter item quantity: "))
                    self.add_item(item_id, item_name, item_price, item_quantity)
                elif choice == 2:
                    item_id = int(input(">>> Enter item ID: "))
                    self.remove_item(item_id)
                elif choice == 3:
                    self.add_customer()
                elif choice == 4:
                    self.show_customers()
                elif choice == 5:
                    customer_id = int(input(">>> Enter customer ID: "))
                    self.remove_customer(customer_id)
                elif choice == 6:
                    self.show_menu()
                elif choice == 7:
                    item_id = int(input(">>> Enter item ID: "))
                    item_price = int(input(">>> Enter new item price in BDT: "))
                    self.set_item_price(item_id, item_price)
                elif choice == 8:
                    print("\n >>> Exiting the admin menu.\n")
                    break
                else:
                    print(">>> Please enter a valid choice between 1 and 8.")
            except ValueError:
                print("\n >>> Invalid input. Please enter a number between 1 and 8.\n")

# --------------------------- Admin code end from here ---------------------------------


# --------------------------- Customer code start from here ---------------------------------
class Order:
    def __init__(self, item_name, item_price, item_quantity, date_time):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity=item_quantity
        self.date_time = date_time

    def __repr__(self):
        return (f"Item name: {self.item_name}\nItem price: {self.item_price} Taka\nDate time: {self.date_time}")


class Customer:
    order_list = []
    wallet = 250
    past_order=[]
    date_time = datetime.datetime.now()

    @classmethod
    def create_new_account(self, customer_id, name, email, address):
        new_customer = Add_Customer(customer_id=customer_id, name=name, email=email, address=address)
        Admin.customer_list.append(new_customer)
        print("\n------- Account created successfully !! ---------")

    @classmethod
    def create_account(self):
        customer_id = random.randint(1, 700)
        name = input(">>> Enter your full name: ").lower()
        email = input(">>> Enter your valid email: ").lower()
        address = input(">>> Enter your current address: ")

        for customer in Admin.customer_list:
            if customer.email == email:
                print("\n >>> This email is already used. Try another email <<< \n")
                return

        self.create_new_account(customer_id, name, email, address)

    @classmethod
    def order_item(self):
        Admin.show_menu()
        if not Admin.menu_list:
            print("\n >>> Menu is empty. No items available. \n")
            return

        item_name = input(">>>> Enter your item name to place an order: ").upper()
        item_quantity=int(input("\n >>> Enter your item quantity: "))
        
        for item in Admin.menu_list:
            if item_name == item.item_name :
                if  item.item_quantity >= item_quantity:
                    item_price = item.item_price
                    item.item_quantity = item.item_quantity - item_quantity
                    new_order = Order(item_name=item_name, item_price=item_price, item_quantity=item_quantity, date_time=self.date_time)
                    self.order_list.append(new_order)
                    print("\n -------- Your order has been placed successfully ------- \n")
                    return
                else:
                    print("\n >>>> Item quantity is not available <<<<\n")

            else:
                print("\n >>> Item is not available in the menu. \n")

    @classmethod
    def check_available_balance(self):
        print(f"\n>> Your available balance is: {self.wallet} Taka\n")

    @classmethod
    def total_price(self):
        total_bill = 0
        for order in self.order_list:
            total_bill = total_bill + (order.item_quantity * order.item_price)
            
        print(f"\n >>>>> Your total bill is {total_bill} taka !! <<<<<<< \n")

    @classmethod
    def past_orders(self):
        if not self.past_order:
            print("\n >>> Past orders are not available!\n")
            print("\n >>> Note: You can see past orders, \n >>> After paid for your items.\n")
            return
        print("\n >>> List of past orders <<< \n")
        for order in self.past_order:
            print(order)
            print()
            
    
    @classmethod
    def orders(self):
        if not self.order_list:
            print("\n >>> Orders are not available!\n")
            return
        print("\n >>> List of orders <<< \n")
        for order in self.order_list:
            print(order)
            print()
            
        self.total_price()
        
    @classmethod
    def add_funds(self):
        try:
            funds = int(input("Enter your amount: "))
            self.wallet += funds
            print(f"\n >>> Your new balance is {self.wallet} Taka.\n")
        except ValueError:
            print("\n >>> Please enter a valid numeric amount.\n")

        
    @classmethod
    def pay_bill(self):
        self.total_price()
        total=0
        for order in self.order_list:
            total=total+(order.item_price * order.item_quantity)  
        total_money = int(total)
        
        try:
            amount = int(input("\n >>> Enter the amount to pay: "))
            if self.wallet >= total_money:
                if amount == total_money:
                    self.wallet -= total_money
                    self.past_order=self.order_list
                    self.order_list=[]
                    print("\n >>>> Bill paid successfully <<<< \n")
                    
                else:
                    self.total_price()
            else:
                print("\n >>> Insufficient amount. Please add more funds or enter the correct amount.\n")
        except ValueError:
            print("\n >>> Please enter a valid numeric amount.\n")

    @classmethod
    def customer_menu(self):
        while True:
            print("\n >>-------->> Welcome Dear Customer <<-----------<<\n")
            print("1. View the restaurant menu")
            print("2. Place an order")
            print("3. Check available balance")
            print("4. View list of orders")
            print("5. View list of past orders")
            print("6. Add funds to your balance")
            print("7. Pay bill for items")
            print("8. Exit from customer menu \n")

            try:
                choice = int(input(">>> Enter your choice: "))

                if choice == 1:
                    Admin.show_menu()
                elif choice == 2:
                   self.order_item()
                elif choice == 3:
                   self.check_available_balance()
                elif choice == 4:
                    self.orders()
            
                elif choice == 5:
                     self.past_orders()
                     
                elif choice == 6:
                   self.add_funds()
                elif choice == 7:
                   self.pay_bill()
                elif choice == 8:
                    print("\n >>> You exited from the customer menu. \n")
                    break
                else:
                    print(">>> Please enter a choice between 1 and 7.\n")
            except ValueError:
                print("\n >>> Invalid input. Please enter a numeric choice.\n")

# --------------------------- Customer code end from here ---------------------------------



# --------------------------- Restaurant code start from here ---------------------------------

class Admin_Menu:
      @staticmethod
      def admin_menu():
       Admin.admin_menu()
       
class Customer_Menu:
    @staticmethod
    def customer_menu():
        Customer.customer_menu()
             
class Restaurant:
      
    @staticmethod
    def register_or_login_admin():
           print("\n -------- Press L for login and R for register  -------- \n")
           option = input("Enter your choice: ")
           
           if option.lower()=='l':
               name = input(">>> Enter your name: ").lower()
               email = input(">>> Enter your email: ").lower()
               message=""
               
               if Admin.admin_list:
                   
                 for admin in Admin.admin_list:
               
                   if admin.name==name and admin.email == email:
                      print("\n >>>------- Log in successful ----------<<<")
                      Admin_Menu.admin_menu()
                      break
                  
                   elif admin.name!=name and admin.email != email:
                     message="\n --------- Sorry!! Your provided information invalid create an account or try again !! ---------\n"
        
                   else:
                     message="\n --------- Sorry!! email or name was wrong try again !! ---------\n"

               else:
                   message="\n >>>>> Admin not available create an account <<<<<\n"

               print(message)   
                      
           elif option.lower()=='r':
               
            Admin.create_account()
            Admin_Menu.admin_menu()
            
           else:
               print("\n ---- Please enter valid option ---- \n") 
    
    @staticmethod
    def register_or_login_customer():
           print("\n -------- Press L for login and R for register  -------- \n")
           option = input("Enter your choice: ")
           
           if option.lower()=='l':
               name = input(">>> Enter your name: ").lower()
               email = input(">>> Enter your email: ").lower()
               message=""
               
               if Admin.customer_list:
                   
                 for customer in Admin.customer_list:
                   if customer.name == name and customer.email == email:
                       print("\n >>>------- Log in successful ----------<<<")
                       Customer.customer_menu()
                       break
                    
                   elif customer.name != name and customer.email != email:
                     message="\n --------- Sorry!! Your provided information invalid create an account or try again!! ---------\n"
                 
                   else:
                     message="\n --------- Sorry!! email or name was wrong try again !! ---------\n"

               else:
                   message="\n >>>>> Customer not available create an account <<<<<\n"

               print(message)   
                      
           elif option.lower()=='r':
               
            Customer.create_account()
            Customer.customer_menu()
            
           else:
               print("\n ---- Please enter valid option ---- \n") 
               
    while True:
        print("\n1.------------- Register or log in as a Customer. ----------o ")
        print("2.---------- Register or log in as a Admin. ----------o ")
        print("3.---------- Exit from restaurant ----------o ")
        
        choice = input("\n >>> Enter your choice: ")
        choice_int = int(choice)
        
        if choice_int == 1 :
         register_or_login_customer() 
          
        elif choice_int==2:
          register_or_login_admin()   
            
        elif choice_int==3:
            print("\n >>> You are exited from the restaurant \n ")
            break
        else:
            print("\n >>> Please enter your choice between 1 to 3 !!")
            
 # --------------------------- Restaurant code end from here ---------------------------------


