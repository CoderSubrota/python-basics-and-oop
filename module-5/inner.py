def checkAge():
    def check(age):
        if age > 20:
            print("You are ready to go")
        else:
            print("You are not ready to got")
            
    return check

result = checkAge()(25)

        
def first_func():
    def first_nested(age):
        def second_nested(min_age):
            def third_nested(max_age):
                if age > max_age:
                    print("Max age")
                elif age > min_age :
                    print("Your age is minimum")
                else:
                    print("You are a child")
            return third_nested
        return second_nested
    return first_nested

res = first_func()(35)(20)(32)
            