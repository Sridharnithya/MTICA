s1=input().split()
s2=input().split()
print(*[(int(i)+int(j)) for i,j in zip(s1,s2)])
