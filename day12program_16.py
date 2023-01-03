class Number:
    num=''
    def __init__(self,num):
        self.num=num
    def checkEvenorOdd(self):
        if self.num%2==0:
            return "Even Number"
        else:
            return "Odd Number"
    def calculateFactorial(self):
        if self.num==0:
            return 1
        res=1
        for i in range(1,self.num+1):
            res*=i
        return res
    def sumOfDigits(self):
        if self.num<0:
            self.num=abs(self.num)
        temp=str(self.num)
        t=0
        for i in temp:
            t+=int(i)
        return t
    def checkArmStrongNumber(self):
        n=str(self)
        n=len(self)
        total=0
        for i in num:
            total += int(i)**n
        if int(num)==total:
            return 1
        else:
            return 0
inp=int(input())
ob=Number(inp)
print('Factorial of',inp,'is',ob.calculateFactorial())
print(inp,"is",ob.checkEvenorOdd())
print('sum of Digits of',inp,'is',ob.sumOfDigits())
print(inp,"is",ob.checkArmStrongNumber())
