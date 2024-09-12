import sys
input = sys.stdin.readline

n = int(input())
s = list(int(input()) for _ in range(n))

s.sort(reverse=True)
result = 0

for i in range(1,n+1):
    if s[i-1] - (i-1) > 0:
        result += s[i-1] - (i-1)



print(result)