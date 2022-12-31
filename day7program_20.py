Lst1=[11,22,33,44,55]
Lst2=[1,2,3,4,5]
Lst3=[5,6,5,2,1,3,2,3]

##def add(a,b):
##    return a+b
##ans=list(map(add,Lst1,Lst2))
print(Lst1)
print(Lst2)
print(Lst3)
##print(ans)

##print('-'*40)
ans=list(map(lambda a,b,c:a+b+c,Lst1,Lst2,Lst3))
print(ans)
