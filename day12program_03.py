sample_set={"Yellow","Orange","Black"}
sample_List=["Blue","Green","Red"]
sample_set.update(sample_List)
print(sample_set)

#unhashable type can't be set member
for i in sample_List:
    sample_set.add(i)
