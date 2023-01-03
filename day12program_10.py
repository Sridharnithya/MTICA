class Student:
    College='MTICA'
    Course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print('Name:'+self.name+'\nRoll.No:'+str(self.rollno))
        print('College:'+self.College+'\nCourse: '+str(self.Course))
for i in range(3):
    n=input()
    r=int(input())
    obj=Student(n,r)
    obj.displayStudent()
    
    
