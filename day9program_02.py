def PrintSeriesDecreasing(ch,n):
    assert isinstance(ch,str),"First Argument should be String"
    assert isinstance(ch,int),"Second Argument should be String"
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpCh=input("Enter a character:")
inpNum=int(input("Enter a no:"))
try:
    PrintSeriesDecreasing(inpCh,inpNum)
except AssertionError as obj:
    print (obj)
print('-'*40)
PrintSeriesDecreasing(inpCh,inpNum)

    
