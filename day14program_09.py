class A:
    def first_method(self):
        print("Method of class A ...")
class B:
    def first_method(self):
        print("Method of class B ...")
class C(B,A):
    def third_method(self):
        print("Method of class C ...")
        super().first_method()
if __name__=='__main__':
    ob=C()
    ob.first_method()
    ob.third_method()
    #C().third_method()
#Circular inheritances is not possible.
    
    
