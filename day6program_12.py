string='''
practice problems for list com pre hension in python.'''
##ans=[]
wordsList=string.split(' ')
##for i in wordsList:
##    if len(i)<5:
##        ans.append(i)
##print(*ans)

ans=[i for i in wordsList if len(i.strip('\n'))==8 ]
print(*ans)


##ans=[i for i in wordsList if len(i)==3 ]
##print(*ans)
