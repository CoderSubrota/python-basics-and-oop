
marks=int(input())
if marks > 0 and marks < 100 :
    
    if marks >= 80 and marks <= 100:
        print("A+")
    elif marks >=70 and marks < 80:
        print("A")
    elif marks >=60 and marks < 70:
        print("A-")
    elif marks >=50 and marks < 60:
        print("B")
        
    elif marks >=45 and marks < 50:
        print("C")
        
    elif marks >=33 and marks < 45:
        print("D")
    else:
        print("Failed Good luck for the next time")
        
else:
    print("Invalid number enter number between 0 to 100")
