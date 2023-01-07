lst=[1,2,3,4]
it=iter(lst)#this builds an iterator object
#print (next(it)) #prints next available element in iterator
#Iterator object can be traversed using regular for statement
for x in it:
    print(x,end=" ")
##for using next() function
import sys
while True:
    try:
        print(next(it))
    except StopIteration as ob:
        print(ob)
        break
        #sys.exit()#you have to import sys module for this
