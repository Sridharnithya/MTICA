def Fact(num):
    assert(isinstance(num,int)),"Factorial not defined for non integer"
    assert (num >=0),"Factorial of negative number is not defined!"
    if num==0:
        return 1
    else:
        return num*Fact(num-1)
try:
    print (Fact(-45))
except Exception as ob:
    print(ob)
try:
    print (Fact(4.9))
except Exception as ob:
    print(ob)
try:
    print (Fact(45))
except Exception as ob:
    print(ob)
try:
    print (Fact('today'))
except Exception as ob:
    print(ob)
