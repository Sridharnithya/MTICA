employees=['Sanya','Sivaangi','Aliya']
defaults={"designation": 'Developer',"Salary":80000}
data=dict.fromkeys(employees,defaults)
print(data)
print(data["Sivaangi"])
