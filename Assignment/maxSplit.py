def getMaxSplit (S):
    count = 0
    balance =0
    result = []
    cur_str = ""
    for str in S:
        cur_str+=str 
        if str == "R":
            balance +=1
        else:
            balance-=1
            
        if balance==0:
            result.append(cur_str)
            cur_str=""
            count+=1
            
    print(count)
    
    for s in result:
         print(s)
        
S = input()
getMaxSplit(S)
