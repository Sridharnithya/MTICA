sample_dict= {
    "name": "Sivaangi",
    "age": 21,
    "salary": 100000,
    "city": "Chennai"}
keys=["name","salary"]
res=dict()
for k in keys:
    res.update({k: sample_dict[k]})
print(res)
