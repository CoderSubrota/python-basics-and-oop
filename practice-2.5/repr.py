class Shop:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        
result = Shop("Subrota","subrota45@gmail.com")
print(result.name,result.email)


class Person:
    def __init__(self,name,email,city):
        self.name=name
        self.email=email
        self.city=city
        
    def __repr__(self): 
       return f"{self.name} {self.email} {self.city}"
resu = Person("Subrota", "subrota78@gmail.com", "Rajshahi")

print(resu)
