def PrintSeries(n):
    
    for i in range(1,n+1):
        print()
        for j in range(i):
            print(i,end=' ')
            
    return None
inpNum=int(input())
PrintSeries(inpNum)
