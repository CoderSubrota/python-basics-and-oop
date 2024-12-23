class Add:
    def __init__(self, num,num2):
        self.num=num
        self.num2=num2
        
    def __add__(self,other):
        return (
                f"First number: {self.num} Second number: {self.num2}\n"
                f"Addition first : {self.num+self.num2} Addition second : {other.num+other.num2}\n"
                f"Addition Cross: {self.num+other.num2} Second: {self.num2+other.num}"

        )
add = Add(12,32)
add2=Add(23,45)

result = add + add2

print(result)
