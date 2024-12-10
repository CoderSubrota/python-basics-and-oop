from collections import Counter
def checkRemovals(a):
    countElements = Counter(a) 
    removals = 0
    for element,count in countElements.items() :
         if count < element:
             removals += count
         else :
             removals+= count - element
             
    return removals 
             
n = int(input())
a = input().split()
arr = [int(element) for element in a] 
result = checkRemovals(arr) 

print(result) 
