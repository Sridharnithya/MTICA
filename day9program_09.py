def PrintDay(dn):
    mn=' '
    if(dn==1):
        mn="Sunday"
    elif(dn==2):
        mn="Monday"
    elif(dn==3):
        mn="Tuesday"
    elif(dn==4):
        mn="Wednesday"
    elif(dn==5):
        mn="Thursday"
    elif(dn==6):
        mn="Friday"
    elif(dn==7):
        mn="Saturday"
    return mn
import time
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(PrintDay(inpNum))
    print(time.time()-start)
    start=time.time()
    print(PrintDay(inpNum))
    print(time.time()-start)
    
