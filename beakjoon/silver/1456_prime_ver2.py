import sys
import math

input = sys.stdin.readline
n,m = map(int,input().split())

max_limit = int(math.sqrt(m))+1
A = [True] * (max_limit+1)
A[0] = A[1] = False

for i in range(2, int(math.sqrt(max_limit))+1):
    if A[i]:
        for j in range(i*i, max_limit+1, i):
            A[j] = False

count = 0

for i in range(2, max_limit+1):
    if A[i]:
        temp = i * i
        while temp <= m:
            if temp >= n:
                count += 1
            if temp > m //i:
                break
            temp *= i
print(count)