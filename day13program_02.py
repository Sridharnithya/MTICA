def printBlue():
    print('you choose blue!\n')
    return
def printRed():
    print('you chose red!\n')
def printOrange():
    print('you chose orange!\n')
def printYellow():
    print('you chose yellow!\n')
def choice():
    print("0:Blue")
    print("1:red")
    print("2:orange")
    print("3:yellow")
    print("4:Quit")
    return
ColorSelect={0:printBlue,1:printRed, 2:printOrange, 3:printYellow }
selection=0
while True:
    if selection ==4:break
    choice()
    selection=int(input("select a color option:"))
    if (selection>=0) and (selection<4):
        ColorSelect[selection]()
    
