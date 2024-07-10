import sys
import math
input = sys.stdin.readline

n,m = map(int,input().split())
A = [0] * 1000001

for i in range(len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)))+1):
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i):
        A[j] = 0

count = 0

for i in range(len(A)):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= m / temp:
            if A[i] >= n / temp:
                count += 1
            temp = temp * A[i]


print(count)