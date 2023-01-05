class Animal:  #superclass
    def __init__(self,name,color):
        self.color=color
        self.name=name
        #CAt and Dog are subclass.
class Cat(Animal): 
    def mew(self):
        print("Cat meows")
class Dog(Animal):
    def bark(self):
        print("Woof")
if __name__=="__main__":
    print(__name__)
    pet1=Dog("Tommy","brown")
    pet2=Cat("lucy","white")
    pet1.bark()
    pet2.mew()
    print(pet1.name)
    print(pet2.name)
    
