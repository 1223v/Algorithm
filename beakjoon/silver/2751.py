import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = [0] * int(N)

for i in range(N):
    A[i] = int(input())

A.sort()
print('\n'.join(map(str,A)))