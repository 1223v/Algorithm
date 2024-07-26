import sys
input = sys.stdin.readline

n = int(input())
A = []

for _ in range(n):
    temp = int(input())
    A.append(temp)

A.sort()

result = []
for i in A:
    result.append(i*n)
    n -= 1

print(max(result))