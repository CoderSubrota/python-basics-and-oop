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
    