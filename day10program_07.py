fo=open(r"D:\pythonpractice41\day10\MCA.txt","a")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("Written to file")
