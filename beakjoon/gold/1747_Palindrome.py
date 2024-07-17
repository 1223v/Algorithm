import sys
import math

N = int(input())
A = [0] * (10000001)

for i in range(2,len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A))+1)):
    if A[i] == 0:
        continue
    for j in range(i*i, len(A), i):
        A[j] = 0

def isPalidrome(target):
    temp = list(str(target))
    s=0
    e=len(temp)-1
    while s<e:
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True

i = N

while True: # N부터 1씩 증가시키면서 소숭와 팰린드롬 수가 맞는지 판별
    if A[i] != 0:
        result = A[i]
        if isPalidrome(result):
            print(result)
            break

        i += 1
