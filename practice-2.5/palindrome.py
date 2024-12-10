# get input from users 
numbers = input() 
# reverse the number and convert into integer
reverse_numbers = int(numbers[::-1])
print(reverse_numbers) 
# check the numbers is it palindrome or not
if numbers == numbers[::-1] :
    print("YES")
else:
    print("NO")
