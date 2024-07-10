import sys
import math
input = sys.stdin.readline

n, m = map(int,input().split())
A = [0] * (m+1)

for i in range(2,m+1):
    A[i] = i

for i in range(2, int(math.sqrt(m))+1):
    if A[i] == 0: # 이미 소수가 아닌걸로 판명이 난 경우 : 6 = 2 * 3 이므로 2에서 이미 판명됌
        continue

    for j in range(i+i, m+1, i): # 2, 3, 5 등 2에서 안걸리고 3에서도 안걸린 소수들의 배수들은 소수가 아니므로 삭제
        A[j] = 0

for i in range(n, m+1):
    if A[i] != 0:
        print(A[i])