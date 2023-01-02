def printpattern(ch,n):
    assert(n>=0),'INVALID'
    for i in range(n+1):
        print(ch*i)
ch=input()
n=int(input())
try:
    printpattern(ch,n)
except AssertionError as a:
    print(a)
    
