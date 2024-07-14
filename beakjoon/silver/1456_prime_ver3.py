import sys
import math

n,m = map(int,input().split())
max_limit = int(math.sqrt(m))
A = [0] * (max_limit+1)

for i in range(max_limit+1):
    A[i] = i

for i in range(2, int(math.sqrt(max_limit))+1):
    if A[i] == 0:
        continue
    for j in range(i*i, max_limit+1, i):
        A[j] = 0

count = 0

for i in range(2, max_limit+1):
    if A[i] != 0:
        temp = i * i
        while temp <= m:
            if temp >= n:
                count += 1
            if temp > m//i:
                break
            temp *= i

print(count)