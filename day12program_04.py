set1={10,20,30,40,50}
set2={30,40,50,60,70}

##print(set1.intersection(set2))
##print(set1.union(set2))
###remove duplicates
##print(set1^set2)

set1.intersection_update(set2)
print(set1)
