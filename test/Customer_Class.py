from Admin_Class import Admin, Add_Customer
import datetime
import random

class Order:
    def __init__(self, item_name, item_price, date_time):
        self.item_name = item_name
        self.item_price = item_price
        self.date_time = date_time

    def __repr__(self):
        return (f"Item name: {self.item_name}\nItem price: {self.item_price} Taka\nDate time: {self.date_time}")


class Customer:
    order_list = []
    wallet = 0
    
    date_time = datetime.datetime.now()

    @classmethod
    def create_new_account(self, customer_id, name, email, address):
        new_customer = Add_Customer(customer_id=customer_id, name=name, email=email, address=address)
        Admin.customer_list.append(new_customer)
        print("\n------- Account created successfully !! ---------")

    @classmethod
    def create_account(self):
        customer_id = random.randint(1, 700)
        name = input(">>> Enter your full name: ")
        email = input(">>> Enter your valid email: ")
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
                    new_order = Order(item_name=item_name, item_price=item_price, date_time=self.date_time)
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
        total = sum(order.item_price for order in self.order_list)
        print(f"\n >>>>> Your total bill is {total} Taka !! <<<<<<< \n")

    @classmethod
    def past_orders(self):
        if not self.order_list:
            print("\n >>> Previous orders are not available!\n")
            return
        print("\n >>> List of past order <<< \n")
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
        total = sum(order.item_price for order in self.order_list)
        try:
            amount = int(input("\n >>> Enter the amount to pay: "))
            if self.wallet >= total:
                if amount == total:
                    self.wallet -= total
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
            print("4. View list of past orders")
            print("5. Add funds to your balance")
            print("6. Pay bill for items")
            print("7. Exit from customer menu \n")

            try:
                choice = int(input(">>> Enter your choice: "))

                if choice == 1:
                    Admin.show_menu()
                elif choice == 2:
                   self.order_item()
                elif choice == 3:
                   self.check_available_balance()
                elif choice == 4:
                   self.past_orders()
                elif choice == 5:
                   self.add_funds()
                elif choice == 6:
                   self.pay_bill()
                elif choice == 7:
                    print("\n >>> You exited from the customer menu. \n")
                    break
                else:
                    print(">>> Please enter a choice between 1 and 7.\n")
            except ValueError:
                print("\n >>> Invalid input. Please enter a numeric choice.\n")


