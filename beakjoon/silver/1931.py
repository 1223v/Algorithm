import sys
input = sys.stdin.readline

N = int(input())
A = [[0,0] for _ in range(N)]

for i in range(N):
    s,e = map(int,input().split())
    A[i][0] = e
    A[i][1] = s


A.sort()
result = 0
end = -1

for i in range(N):

    if A[i][1] >= end:
        end = A[i][0]
        result += 1

print(result)