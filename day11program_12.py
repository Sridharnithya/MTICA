#rename of a dictionary key
sample_dict= {
    "name": "Sivaangi",
    "age": 21,
    "salary": 100000,
    "city": "Chennai"}
sample_dict['location']=sample_dict.pop('city')
print(sample_dict)
