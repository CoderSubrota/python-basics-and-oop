class Student:
    def __init__(self,name,email):
        self.name = name
        self.__email=email
        
    @property
    def get_email(self):
        return self.__email, self.name
    
    @property
    def name_set(self): 
        return self.name
    
    @name_set.setter
    def set_name(self,value):
        if value=="":
            print("Name can not be empty!!")
        else:
         self.name = value
         
    @set_name.getter 
    def get_name(self):
        return self.name     
    
    @staticmethod
    def add_method(first,second):
        return f"{first+second}"
    
stud = Student("Subrota","subrota78@gmail.com")
(name,email)=stud.get_email
print(name,email)
print(stud.name)
print(stud.add_method(45,58))
stud.set_name="Johan play boy"
print(stud.name)

