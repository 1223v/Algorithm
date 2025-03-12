import sys
input = sys.stdin.readline

s = input()
num = ["","","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
result = 0
for i in range(len(s)):
    for j in range(3,len(num)):
        if s[i] in num[j]:
            result += j

print(result)
