print()
print('Aishu')
print('sanya',97)
print('Sivaangi',97,'Kavya')
##variable length argument
def add(*n):
    temp=0
    for i in n:
        temp+=i
    return temp
print("add():",add())
print("add(5):",add(5))
print("add(5,7):",add(5,7))
print("add(5,7,2,11,55,77,22):",add(5,7,2,11,55,77,22))

