def minimizeNumbers(A):
    minimumOperation = 31
    for element in A:
        operationCount=0
        while element%2==0:
            element //=2
            operationCount+=1
        minimumOperation = min(minimumOperation, operationCount)
    return minimumOperation 

N = int(input())
A = input().split() 
Arr = [int(element) for element in A]
result = minimizeNumbers(Arr)
print(result)
