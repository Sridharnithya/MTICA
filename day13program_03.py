def printSunday():
    print('Sunday')
    return
def printMonday():
    print('Monday')
def printTuesday():
    print('Tuesday')
def printWednesday():
    print('Wednesday')
def printThursday():
    print('Thursday')
def printFriday():
    print('Friday')
def printSaturday():
    print('Saturday')
def choice():
##    print("0:Sunday")
##    print("1:Monday")
##    print("2:Tuesday")
##    print("3:Wednesday")
##    print("4:Thursday")
##    print("5:Friday")
##    print("6:Saturday")
##    print("7:Quit")
    print("Enter day number between 1-7")
    return
dayDict={0:printSunday,1:printMonday, 2:printTuesday, 3:printWednesday,
           4:printThursday,5:printFriday,6:printSaturday }
##selection=0
##while True:
##    if selection ==6:break
##    choice()
##    selection=int(input("select a Day option:"))
##    if (selection>=0) and (selection<4):
##        DaySelect[selection]()
##    

dayNo=int(input())
if dayNo<=1 and dayNo<=7:
    dayDict[dayNo]()
else:
    print("INVALID")
    

