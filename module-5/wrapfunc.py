def myFunc(getFunc):
     res = getFunc(25,56)
     print(res)
     
     print("My func")


def myTest(num,num2):
      print("My test")
      return num+num2


res = myFunc(myTest)
