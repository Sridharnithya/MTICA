class Rectangle:
    length='l'
    width='w'
    def __init__(self,l,w):
        assert(l>=0 and w>=0),'INVALID'
        self.l=l
        self.w=w
    def calculatePerimeter(self):
        temp=2*self.l+self.w
        return temp
    def calculateArea(self):
        temp=self.w*self.l
        return temp
l=int(input('l:'))
w=int(input('w:'))
try:
   ob=Rectangle(l,w)
   Area=ob.calculateArea( )
   Peri=ob.calculatePerimeter( )
   print('Area of Rectangle is',Area)
   print('Perimeter of Rectangle is',Peri)
except AssertionError as obj:
    print(obj)
