import sys
input = sys.stdin.readline

N = int(input())
A = []
MAX = 0

for i in range(N):
    A.append((int(input()), i))

sorted_A = sorted(A)

for i in range(N):
    if MAX < sorted_A[i][1] - i:
        MAX = sorted_A[i][1] - i

print(MAX+1)