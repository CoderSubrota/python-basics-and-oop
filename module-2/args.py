def myArgs(firstName, lastName):
    fullName = f'{firstName} {lastName}'
    return fullName
result = myArgs("Subrota", "Chandra")
print(result)



def myArgs2( *name):
    return name
result2 = myArgs2("Subrota", "Chandra", "Bijoy", "Ajay")
print(result2)


 
def myArgs3( firstName, **lastName):
    
    return f'{firstName} {lastName}'
 
result3 = myArgs3(firstName="Subrota", lastName="Sarker", midName="Chandra")

print(result3)

