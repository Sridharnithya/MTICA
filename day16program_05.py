def reverseString(s):
    ans={i[::-1] for i in s}
    return ans
inp=input().split()
print(*reverseString(inp))
