A,B = input().split()
A_int = int(A)
B_int = int(B)
found = False
for number in range(A_int, B_int+1):
    number_string = str(number)
    is_lucky =  True
    for digit in number_string:
        if digit!='4' and digit!='7':
            is_lucky = False
            break
    if is_lucky:
       print(number, end=" ")
       found = True 
  
if not found:
    print(-1)
    
# 7 4 44 77 47 74