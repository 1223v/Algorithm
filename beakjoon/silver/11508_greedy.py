import sys
input = sys.stdin.readline

n = int(input())
s = list(int(input()) for _ in range(n))
s.sort(reverse=True)
result = 0
for i in range(n):
    if (i+1) % 3 !=0:
        result += s[i]

print(result)