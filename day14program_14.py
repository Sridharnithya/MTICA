#magic methods "dunders"
#are special methods which have leading and trailing double underscore
#used for operator overloading.

#Multiply Method
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __mul__(self,ob):
        temp=(self.real*ob.real-self.imag*ob.imag,
              self.real*ob.imag+self.imag*ob.real)
        return temp
    def __str__(self):
        return(self.real,self.imag)
ob1=Complex(3,5)
ob2=Complex(2,1)
ob3=ob1*ob2
print(ob3)
