class person:
      name="Subrota Chandra"
      age = 23
      profession = "Web developer"
print(person.name)
print(person.age)
print(person.profession)

class Student:
     infor = []
     def studentInfo(self, name,age,class_name,city):
           self.info = []
           self.name = name
           self.age = age
           self.class_name= class_name
           self.city = city
           self.info.append(name)  
           self.info.append(age)  
           self.info.append(class_name)  
           self.info.append(city)  
           self.infor.append(name)  
           self.infor.append(age)  
           self.infor.append(class_name)  
           self.infor.append(city)  
student = Student() 
student.studentInfo("Subrota", 23, "Honours third year", "Joypurhat")
student2 = Student()
student2.studentInfo("Bijoy", 22, "Honours first year", "Khulna")

student3 = Student()
student3.studentInfo("Ghush", 22, "Honours second year", "Rajshahi")

print(student.info)
print(student2.info)
print(student3.info)

student3 = Student()
print(student3.infor)
