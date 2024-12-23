import random

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
                f"Name: {self.name}\n"
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
        name = input(">>> Enter your full name: ")
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
        name = input(">>> Enter customer name: ")
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
            print("7. Update item price")
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


