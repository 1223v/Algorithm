import sys
import heapq
input = sys.stdin.readline

n = int(input())
result = 0
A = [list(map(int,input().split())) for _ in range(n)]
A.sort()

hq = [A[0][1]]
for i in range(1,n):
    if hq and A[i][0] >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq,A[i][1])

print(len(hq))
