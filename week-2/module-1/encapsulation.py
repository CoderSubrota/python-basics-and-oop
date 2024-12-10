class first:
     def __init__(self, name, email):
         self.__name = name #private
         self.__email = email
     def get_name(self):
         return self.__name
     def get_email(self):
         return self.__email
         
class second(first):
    def __init__(self, name, email, country):
        self.__country = country
        super().__init__(name, email)
        
    def get_country(self):
        return self.__country 
    
class third(second):
    def __init__(self, name, email, country, gender):
        self.__gender = gender
        super().__init__(name, email, country)
    def get_gender(self):
        return self.__gender
    
        
class forth(third):
    def __init__(self, name, email, country, gender, age):
        self.__age = age
        super().__init__(name, email, country, gender)
    def get_age(self):
        return self.__age
     
forthClass = forth("Subrota", "subrota455@gmail.com", "Bangladesh", "Male", 23)

print(forthClass.get_name()) 
print(forthClass.get_email()) 
print(forthClass.get_country()) 
print(forthClass.get_gender()) 
print(forthClass.get_age()) 


        