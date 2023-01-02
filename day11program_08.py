#Rename key of dictionary
sample_dict= {
    "name": "Sivaangi",
    "age": 21,
    "salary": 100000,
    "city": "Chennai"}
keys=["name","salary"]
##newDict={}
##for i in keys:
##    newDict[i]=sample_dict[i]
##print(newDict)
newDict={sample_dict[i] for i in keys}
print(newDict)
