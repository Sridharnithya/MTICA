Lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in Lst:
##    if i*i >=50:
##        ans.append(round(i*i))
##print(ans)

##ans=[i*i for i in Lst if i*i >=50]
##print(ans)


print([i*i for i in Lst if i*i >=50] )
