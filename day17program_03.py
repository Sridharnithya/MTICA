import sys
print("coming through stdout")
save_stdout=sys.stdout
fh=open(r"D:\pythonpractice41\test.txt","w")
sys.stdout=fh
print("this line goes to test.txt")
print(input())
sys.stdout=save_stdout
fh.close()
