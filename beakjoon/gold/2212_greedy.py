# https://www.acmicpc.net/problem/2212
# 다시 풀어볼 문제
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
s = list(map(int,input().split()))
s.sort()

if K >= N:
    print(0)
    exit()

dist = []
for i in range(1,N):
    dist.append(s[i]-s[i-1])

dist.sort(reverse=True)

for i in range(K-1):
    dist.pop(0)

print(sum(dist))