import sys
input = sys.stdin.readline

n,m = map(int,input().split())

A = [input().rstrip() for _ in range(n)]

a,b = 0 ,0
for i in range(n):
    if "X" not in A[i]:
        a += 1


for j in range(m):
    if "X" not in [A[i][j] for i in range(n)]:
        b += 1

print(max(a,b))
