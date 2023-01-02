def PrintMonth(dn):
    mn=' '
    if(dn==1):
        mn='January'
    elif(dn==2):
        mn='February'
    elif(dn==3):
        mn='March'
    elif(dn==4):
        mn='April'
    elif(dn==5):
        mn='May'
    elif(dn==2):
        mn='June'
    elif(dn==2):
        mn='July'
    elif(dn==2):
        mn='August'
    elif(dn==2):
        mn='September'
    elif(dn==2):
        mn='October'
    elif(dn==11):
        mn='November'
    elif(dn==12):
        mn='December'
    return mn
for i in range(4):
    inpNum=int(input())
    print(PrintMonth(inpNum))
