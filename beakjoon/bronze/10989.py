import sys

input = sys.stdin.readline

n = int(input())
A = [0] * 10001
for i in range(n):
    A[int(input())] += 1

for i in range(10001):
    if A[i] != 0:
        for j in range(A[i]):
            print(i)
