arr = [21,45,12,6,10]
even = list(filter(lambda x : x %2==0, arr))
for num in even:
    print(num)
    
dic = {"name":"Subrota Chandra Sarker", "age":23, "Education":"Diploma IT"}
dic["name"] = "Bijoy"
del dic["age"] 
for key, value in dic.items() :
    print("key: ", key, "value: ", value)
    
myList = [
    {"name": "Subrota Chandra", "age": 23, "education": "CSE"},
    {"name": "Bijoy Chandra Sarker", "age": 24, "education": "Diploma IT"},
    {"name": "Niloy Chandra Sarker", "age": 20, "education": "Diploma BBE"},
    {"name": "Ajay Chandra Sarker", "age": 22, "education": "Diploma EEE"}
]

# Print the header
print(f"{'Name : ':<28} {'Age : ':<8} {'Education : ':<15}")
print("=" *59)   
for item in myList:
    print(f"{item['name']:<28} ||  {item['age']:<8} || {item['education']:<15}")
print("=" *59)   
    
touple = ("subrota",23,"Programmer","Single")
(name,age,profession,martial_status) = touple
print(name, age, profession, martial_status)



    