class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
    
    def calculatePerimeter(self):
        temp=self.pi*self.radius**2
        return temp
    def calculateArea(self):
        temp=2*self.pi*self.radius
        return temp
r=int(input())
ob=Circle(r)
Area=ob.calculateArea( )
Peri=ob.calculatePerimeter( )
print('Area of circle with radius',r,'is',Area)
print('Perimeter of circle with radius',r,'is',Peri)
