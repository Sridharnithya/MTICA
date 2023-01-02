sample_dict= {
    "name": "Sivaangi",
    "age": 21,
    "salary": 100000,
    "city": "Chennai"}
keys=["name","salary"]
##for k in keys:
##    sample_dict.pop(k)
##print(sample_dict)


d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)
