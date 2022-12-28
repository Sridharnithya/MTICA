dict1={'sedan' : 1500, 'SUV' : 2000, 'pickup' : 2500, 'Minivan': 1600, 'Van':2400,
       'semi': 13600, 'Bicycle': 7,'Motorcycle': 110}
##ans=[]
##for i in dict1:
##    if dict1[i]<5000:
##        ans.append(i.upper())
##print(ans)


##ans=[i.upper() for i in dict1 if dict1[i]<5000]
##print(ans)

print([i.upper() for i in dict1 if dict1[i]<5000])
