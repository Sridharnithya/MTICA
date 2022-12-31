inpL=['anjali','divya','pritam','wasim','gaurav']
def rev_str(a):
    return a[::-1]
outL=list(map(rev_str,inpL))
print(inpL)
print(outL)


##out_L=['ilajna','ayvid','matrip','midaw','varuag']
print('-'*50)

inpL=['anjali','divya','pritam','wasim','gaurav']
outL=list(map(lambda x:x[::-1],inpL))
print(inpL)
print(outL)
