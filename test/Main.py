from Admin_Class import Admin
from Customer_Class import Customer

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
               name = input(">>> Enter your name: ")
               email = input(">>> Enter your email: ")
               message=""
               
               if Admin.admin_list:
                   
                 for admin in Admin.admin_list:
               
                   if admin.name.lower()==name.lower() and admin.email.lower() == email.lower():
                      print("\n >>>------- Log in successful ----------<<<")
                      Admin_Menu.admin_menu()
                      break
                  
                   elif admin.name.lower()!=name.lower() and admin.email.lower() != email.lower():
                     message="\n --------- Sorry!! Your provided information invalid create an account !! ---------\n"
                     break
                 
                   else:
                     message="\n --------- Sorry!! email or name was wrong try again !! ---------\n"
                     break
                 
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
               name = input(">>> Enter your name: ")
               email = input(">>> Enter your email: ")
               message=""
               
               if Admin.customer_list:
                   
                 for customer in Admin.customer_list:
               
                   if customer.name.lower()==name.lower() and customer.email.lower() == email.lower():
                      print("\n >>>------- Log in successful ----------<<<")
                      Customer.customer_menu()
                      break
                  
                   elif customer.name.lower()!=name.lower() and customer.email.lower() != email.lower():
                     message="\n --------- Sorry!! Your provided information invalid create an account !! ---------\n"
                     break
                 
                   else:
                     message="\n --------- Sorry!! email or name was wrong try again !! ---------\n"
                     break
                 
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
            
            
