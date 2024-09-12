import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
s.sort()
result = 0
if len(s) % 2 != 0:
    result = s.pop(-1)

for i in range(len(s)//2):
    result = max(result,s[i]+s[len(s)-1-i])

print(result)


