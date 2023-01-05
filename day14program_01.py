##def solveProblem(s):
##    lst=s.split()
####    return [len(i) for i in lst]
##
##inp=input()
##solveProblem={i:i[::-1] for i in lst}
##print(*solveProblem(inp))

def reverseString(s):
    ans={i:i[::-1] for i in s}
    ans=[i[::-1] for i in s]
    ans=[len(i) for i in s]
    return ans
inp=input().split()
#print(inp)
print(reverseString(inp))
